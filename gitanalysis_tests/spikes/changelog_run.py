from gitanalysis.domain.changelog import Changelog

changelog = Changelog()

with open('gitlog.txt') as f:
    changelog = changelog.fromGitlog(f.read())
    print(changelog.to_csv(index=False))