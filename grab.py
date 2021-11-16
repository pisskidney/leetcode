#!/usr/bin/python3


import json
import requests
import argparse
from typing import Tuple
from os.path import exists


BASE_URL = 'https://leetcode.com/problems/'
GRAPHQL_API_URL = 'https://leetcode.com/graphql'
QUERY = '''query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    boundTopicId
                    title
                    titleSlug
                    content
                    translatedTitle
                    translatedContent
                    difficulty
                    exampleTestcases
                    codeSnippets {
                        lang
                        langSlug
                        code
                    }
                }
            }'''


def get_url() -> str:
    parser = argparse.ArgumentParser(description='Grab leetcode problem')
    parser.add_argument(
        'slug', metavar='slug', type=str, nargs='+',
        help='Slug of the leetcode problem e.g.: two-sum',
    )
    parser.add_argument(
        '--force', action='store_true',
        help='Overwrite the file if it already exists',
    )
    args = parser.parse_args()
    return args.slug[0], args.force


def get_data(slug: str) -> Tuple[str, int, str, str, str]:
    resp = requests.post(GRAPHQL_API_URL, json={
        'query': QUERY,
        'variables': {
            'titleSlug': slug,
        }
    })
    question = json.loads(resp.text)['data']['question']
    difficulty = question['difficulty'].lower()
    nr = question['questionId']
    title = question['title']
    title_slug = question['titleSlug']
    url = f'{BASE_URL}{title_slug}/'

    code = ''
    for snippet in question['codeSnippets']:
        if snippet['langSlug'] == 'python3':
            code = snippet['code']
    return difficulty, nr, title, url, code


def create_file(difficulty: str, nr: int, title: str, url: str, code: str, *, force: bool) -> None:
    filename = f'{difficulty}/{nr}.py'

    if exists(filename) and not force:
        print(f'\n{filename} already exists! Use --force to overwrite.\n')
        return

    with open(filename, 'w') as f:
        f.write('"""\n')
        f.write(f'{nr}. {title}\n')
        f.write('\n')
        f.write(f'{url}\n')
        f.write('"""\n')
        f.write('\n\n')
        f.write(code)
        f.write('...\n')
        f.write((
            '\n\n'
            'def main():\n'
            '    s = Solution()\n'
            '    print(s.xxx())\n'
            '\n\n'
            "if __name__ == '__main__':\n"
            '    raise(SystemExit(main()))'
        ))

    print(f'Created {filename}\n')


def main() -> int:
    slug, force = get_url()
    difficulty, nr, title, url, code = get_data(slug)
    create_file(difficulty, nr, title, url, code, force=force)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
