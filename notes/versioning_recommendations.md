# Versioning Recommendations

For example, v0.0.0, v1.12.134, v8.0.5-pre, and v2.0.9+meta are valid versions.

Each part of a version indicates whether the version is stable and whether it is compatible with previous versions.

1. The major version must be incremented and the minor and patch versions must be set to zero after a backwards incompatible change is made to the module's public interface or documented functionality, for example, after a package is removed.
2. The minor version must be incremented and the patch version set to zero after a backwards compatible change, for example, after a new function is added.
3. The patch version must be incremented after a change that does not affect the module's public interface, such as a bug fix or optimization.
4. The pre-release suffix indicates a version is a pre-release. Pre-release versions sort before the corresponding release versions. For example, v1.2.3-pre comes before v1.2.3.
5. The build metadata suffix is ignored for the purpose of comparing versions. Tags with build metadata are ignored in version control repositories, but build metadata is preserved in versions specified in go.mod files. The suffix +incompatible denotes a version released before migrating to modules version major version 2 or later (see Compatibility with non-module repositories.

A version is considered unstable if its major version is 0 or it has a pre-release suffix. Unstable versions are not subject to compatibility requirements. For example, v0.2.0 may not be compatible with v0.1.0, and v1.5.0-beta may not be compatible with v1.5.0.
