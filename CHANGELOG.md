# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2021-03-31
### Added
- This changelog.
- Basic unit tests for the library interface in
 `metex/test/test_library.py`.
- Basic test for the script interface in
  `metex/test/test_script_interface.sh`.
- CI configuration in `.gitlab-ci.yml` and `tox.ini`.
- Package manifest in `MANIFEST.in`
- Boilerplate package configuration in pyproject.toml
### Fixed
- Fixed a bug with rectangular beta-horizontal textures, where the
  generated textures would have swapped width and height with respect
  to the desired values.
### Changed
- Renamed COPYING to LICENSE to better adhere to standard practice for
  python packages.


