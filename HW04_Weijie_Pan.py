import requests


def read_github_repo(id):
    url = 'https://api.github.com/users/' + id + '/repos'
    content = requests.get(url)
    repo = content.json()

    if isinstance(repo, dict):  # verify if the user id exist
        print(f"Cannot find the repo with the id: {id}")
        exit()

    elif 'name' not in repo[0].keys():  # verify if the user has any repository
        print(f"There is zero repository in the account: {id}")
        exit()

    else:
        return repo


def read_github_commit(id):
    repo_result = {}
    repo = read_github_repo(id)
    for name in repo:
        url_commit = 'https://api.github.com/repos/' + id + '/' + name['name'] + '/commits'
        result = requests.get(url_commit)
        commit = result.json()
        number = len(commit)
        repo_result[name['name']] = number

    for key, value in repo_result.items():
        print('Repo:', key, 'Number of commits: ', value)
    return repo_result


def main():
    name = input("Please input the github id: ")
    read_github_commit(name)


if __name__ == '__main__':
    main()
