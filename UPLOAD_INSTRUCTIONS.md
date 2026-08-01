# Upload instructions — AISKG_01_Framework

The safest method is to clone the current repository, replace its contents with
this folder, and commit the changes.

```bash
git clone https://github.com/romenmeitei/AISKG_01_Framework.git
cd AISKG_01_Framework
rm -f CITATION.cff.template GITHUB_ROOT_README.md \
  LICENSE_SELECTION_REQUIRED.md REPOSITORY_TEST_STATUS.md
# Copy all files from the upload-ready folder here, preserving directories.
python verify_repository.py
git add -A
git commit -m "Complete reproducibility release v1.0.0"
git push origin main
git tag -a v1.0.0 -m "Publication reproducibility release v1.0.0"
git push origin v1.0.0
```

GitHub's browser uploader also works for these file sizes, but folders such as
`queries/`, `reference_outputs/`, and `.github/workflows/` must be preserved,
and the four obsolete root files must be deleted manually.
