import subprocess
# import git


from pip._internal.vcs import git

# label = subprocess.check_output(["git", "describe"]).strip()
# print(label)

repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

print(repo)
print(sha)


__version__ = '0.0.2'