Hi there, thank you for your interest in contributing!
Please read the contribution guidelines below, before submitting your first pull request to the InvenTree codebase.

## Quickstart

The following commands will get you quickly configure and run a development server, complete with a demo dataset to work with:

### Bare Metal

```bash
git clone https://github.com/inventree/InvenTree.git && cd InvenTree
python3 -m venv env && source env/bin/activate
pip install invoke && invoke
pip install invoke && invoke setup-dev --tests
```

### Docker

```bash
git clone https://github.com/inventree/InvenTree.git && cd InvenTree
docker compose run inventree-dev-server invoke install
docker compose run inventree-dev-server invoke setup-test --dev
docker compose up -d
```

Read the [InvenTree setup documentation](https://docs.inventree.org/en/latest/start/intro/) for a complete installation reference guide.

### Setup Devtools

Run the following command to set up all toolsets for development.

```bash
invoke setup-dev
```

*We recommend you run this command before starting to contribute. This will install and set up `pre-commit` to run some checks before each commit and help reduce errors.*

## Branches and Versioning

InvenTree roughly follow the [GitLab flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) branching style, to allow simple management of multiple tagged releases, short-lived branches, and development on the main branch.

### Version Numbering

InvenTree version numbering follows the [semantic versioning](https://semver.org/) specification.

### Master Branch

The HEAD of the "main" or "master" branch of InvenTree represents the current "latest" state of code development.

- All feature branches are merged into master
- All bug fixes are merged into master

**No pushing to master:** New features must be submitted as a pull request from a separate branch (one branch per feature).

### Feature Branches

Feature branches should be branched *from* the *master* branch.

- One major feature per branch / pull request
- Feature pull requests are merged back *into* the master branch
- Features *may* also be merged into a release candidate branch

### Stable Branch

The HEAD of the "stable" branch represents the latest stable release code.

- Versioned releases are merged into the "stable" branch
- Bug fix branches are made *from* the "stable" branch

#### Release Candidate Branches

- Release candidate branches are made from master, and merged into stable.
- RC branches are targeted at a major/minor version e.g. "0.5"
- When a release candidate branch is merged into *stable*, the release is tagged

#### Bugfix Branches

- If a bug is discovered in a tagged release version of InvenTree, a "bugfix" or "hotfix" branch should be made *from* that tagged release
- When approved, the branch is merged back *into* stable, with an incremented PATCH number (e.g. 0.4.1 -> 0.4.2)
- The bugfix *must* also be cherry picked into the *master* branch.

## Environment
### Target version
We are currently targeting:
| Name | Minimum version |
|---|---|
| Python | 3.9 |
| Django | 3.2 |

### Auto creating updates
The following tools can be used to auto-upgrade syntax that was depreciated in new versions:
```bash
pip install pyupgrade
pip install django-upgrade
```

To update the codebase run the following script.
```bash
pyupgrade `find . -name "*.py"`
django-upgrade --target-version 3.2 `find . -name "*.py"`
```

## Credits
If you add any new dependencies / libraries, they need to be added to [the docs](https://github.com/inventree/inventree/blob/master/docs/docs/credits.md). Please try to do that as timely as possible.


## Migration Files

Any required migration files **must** be included in the commit, or the pull-request will be rejected. If you change the underlying database schema, make sure you run `invoke migrate` and commit the migration files before submitting the PR.

*Note: A github action checks for unstaged migration files and will reject the PR if it finds any!*

## Unit Testing

Any new code should be covered by unit tests - a submitted PR may not be accepted if the code coverage for any new features is insufficient, or the overall code coverage is decreased.

The InvenTree code base makes use of [GitHub actions](https://github.com/features/actions) to run a suite of automated tests against the code base every time a new pull request is received. These actions include (but are not limited to):

- Checking Python and Javascript code against standard style guides
- Running unit test suite
- Automated building and pushing of docker images
- Generating translation files

The various github actions can be found in the `./github/workflows` directory

### Run tests locally

To run test locally, use:
```
invoke test
```

To run only partial tests, for example for a module use:
```
invoke test --runtest order
```

To see all the available options:

```
invoke test --help
```

## Code Style

Code style is automatically checked as part of the project's CI pipeline on GitHub. This means that any pull requests which do not conform to the style guidelines will fail CI checks.

### Backend Code

Backend code (Python) is checked against the [PEP style guidelines](https://peps.python.org/pep-0008/). Please write docstrings for each function and class - we follow the [google doc-style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for python.

### Frontend Code

Frontend code (Javascript) is checked using [eslint](https://eslint.org/). While docstrings are not enforced for front-end code, good code documentation is encouraged!

### Running Checks Locally

If you have followed the setup devtools procedure, then code style checking is performend automatically whenever you commit changes to the code.

### Django templates

Django are checked by [djlint](https://github.com/Riverside-Healthcare/djlint) through pre-commit.

The following rules out of the [default set](https://djlint.com/docs/linter/) are not applied:
```bash
D018: (Django) Internal links should use the { % url ... % } pattern
H006: Img tag should have height and width attributes
H008: Attributes should be double quoted
H021: Inline styles should be avoided
H023: Do not use entity references
H025: Tag seems to be an orphan
H030: Consider adding a meta description
H031: Consider adding meta keywords
T002: Double quotes should be used in tags
```


## Documentation

New features or updates to existing features should be accompanied by user documentation.

## Translations

Any user-facing strings *must* be passed through the translation engine.

- InvenTree code is written in English
- User translatable strings are provided in English as the primary language
- Secondary language translations are provided [via Crowdin](https://crowdin.com/project/inventree)

*Note: Translation files are updated via GitHub actions - you do not need to compile translations files before submitting a pull request!*

### Python Code

For strings exposed via Python code, use the following format:

```python
from django.utils.translation import gettext_lazy as _

user_facing_string = _('This string will be exposed to the translation engine!')
```

### Templated Strings

HTML and javascript files are passed through the django templating engine. Translatable strings are implemented as follows:

```html
{ % load i18n % }

<span>{ % trans "This string will be translated" % } - this string will not!</span>
```

## Github use
### Tags
The tags describe issues and PRs in multiple areas:
| Area | Name | Description |
| --- | --- | --- |
| Triage Labels |  |  |
|  | triage:not-checked | Item was not checked by the core team  |
|  | triage:not-approved | Item is not green-light by maintainer |
| Type Labels |  |  |
|  | breaking | Indicates a major update or change which breaks compatibility |
|  | bug | Identifies a bug which needs to be addressed |
|  | dependency | Relates to a project dependency |
|  | duplicate | Duplicate of another issue or PR |
|  | enhancement | This is an suggested enhancement, extending the functionality of an existing feature |
|  | experimental | This is a new *experimental* feature which needs to be enabled manually |
|  | feature | This is a new feature, introducing novel functionality |
|  | help wanted | Assistance required |
|  | invalid | This issue or PR is considered invalid |
|  | inactive | Indicates lack of activity |
|  | migration | Database migration, requires special attention |
|  | question | This is a question |
|  | roadmap | This is a roadmap feature with no immediate plans for implementation |
|  | security | Relates to a security issue |
|  | starter | Good issue for a developer new to the project |
|  | wontfix | No work will be done against this issue or PR |
| Feature Labels |  |  |
|  | API | Relates to the API |
|  | barcode | Barcode scanning and integration |
|  | build | Build orders |
|  | importer | Data importing and processing |
|  | order | Purchase order and sales orders |
|  | part | Parts |
|  | plugin | Plugin ecosystem |
|  | pricing | Pricing functionality |
|  | report | Report generation |
|  | stock | Stock item management |
|  | user interface | User interface |
| Ecosystem Labels |  |  |
|  | backport | Tags that the issue will be backported to a stable branch as a bug-fix |
|  | demo | Relates to the InvenTree demo server or dataset |
|  | docker | Docker / docker-compose |
|  | CI | CI / unit testing ecosystem |
|  | refactor | Refactoring existing code |
|  | setup | Relates to the InvenTree setup / installation process |
