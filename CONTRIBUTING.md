# Contributing

Contributions are welcome, and they are greatly appreciated!

Every little bit helps, and credit will always be given.

## Types of Contributions

### Bug Reports, Feature Requests, and Feedback

Create a [new project issue][issue-link]! Try to be as descriptive as possible.

If you are reporting a bug, please include:
* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Bug Fixes, New Features and Documentation

Create a [new merge/pull request][merge-link]! Make sure to follow the guidelines.

Look through the GitHub issues for features, bugs and other requests.
Anything tagged with "help wanted" is open to whoever wants to implement it.

## Get Started!

Ready to contribute? Here's how to set up `typical`
for local development.

1. Fork the `typical` repo on GitHub.
2. Clone your fork locally:
  ```bash
  $ git clone git@github.com:your_name_here/typical.git
  ```
3. Assuming you have pipenv installed, you can **create a new environment
  with all the dependencies** by typing:
  ```bash
  $ make init
  $ pipenv shell
  ```
4. Create a branch for local development:
  ```bash
  $ git checkout -b name-of-your-bugfix-or-feature
  ```
  Now you can make your changes locally.
5. When you're done making changes, check that your changes pass flake8
  and the tests, including testing other Python versions with tox:
  ```bash
  $ make lint
  $ make test
  # Or
  $ make test-all
  ```
6. If your contribution is a bug fix or new feature, you may want to add a test
  to the existing test suite. See section [add a new test](#markdown-header-add-a-new-test) below for details.
7. Commit your changes and push your branch to GitHub:
  ```bash
  $ git add .
  $ git commit -m "Your detailed description of your changes."
  $ git push origin name-of-your-bugfix-or-feature
  ```
8. Submit a pull request through the GitHub website.

## Merge/Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:
1. Make sure to have atomic commits and contextual commit messages!
  [Check out this awesome blog post by Chris Beams for more information.][chris-beams]
2. The pull request should include tests.
3. If the pull request adds functionality, the docs should be updated:
  1. Put your new functionality into a function with a docstring
  2. Add the feature to the list in README.md.

## Add a New Test

When fixing a bug or adding features, it's good practice to add a test
to demonstrate your fix or new feature behaves as expected. These tests
should focus on one tiny bit of functionality and prove changes are correct. 

To write and run your new test, follow these steps:
1. Add the new test to `tests/`. Focus your test on the specific
  bug or a small part of the new feature. 
2. If you have already made changes to the code, stash your changes
  and confirm all your changes were stashed:
  ```bash
  $ git stash
  $ git stash list
  ```
3. Run your test and confirm that your test fails. If your test does not fail,
  rewrite the test until it fails on the original code:
  ```bash
  $ make test
  ```
4. (Optional) Run the tests with tox to ensure that the code changes work
  with different Python versions:
  ```bash
  $ make test-all
  ```
5. Proceed work on your bug fix or new feature or restore your changes. To
  restore your stashed changes and confirm their restoration:
  ```bash
  $ git stash pop
  $ git stash list
  ```
6. Rerun your test and confirm that your test passes.
  If it passes, congratulations!

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

[issue-link]: https://github.com/apehex/typical/issues/new
[merge-link]: https://github.com/apehex/typical/compare
[chris-beams]: http://chris.beams.io/posts/git-commit/
