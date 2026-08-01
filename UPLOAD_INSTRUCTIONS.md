# Upload instructions for AISKG_01_Framework

## Recommended Git command workflow

```bash
git clone https://github.com/romenmeitei/AISKG_01_Framework.git
cd AISKG_01_Framework
# Copy all files from this upload-ready directory into the clone, preserving
# the queries/ and reference_outputs/ directories.
rm -f CITATION.cff.template GITHUB_ROOT_README.md \
      LICENSE_SELECTION_REQUIRED.md REPOSITORY_TEST_STATUS.md
python verify_repository.py
git add -A
git commit -m "Complete Section 1 reproducibility release"
git push origin main
```

## Files to delete from the current public repository

- `CITATION.cff.template`
- `GITHUB_ROOT_README.md`
- `LICENSE_SELECTION_REQUIRED.md`
- `REPOSITORY_TEST_STATUS.md`

They are replaced by the finalized `CITATION.cff`, `README.md`, and `LICENSE`.

## Browser upload

GitHub's browser uploader can add files, but preserve the directory structure
for `queries/` and `reference_outputs/`. Delete the obsolete files listed above
manually. After upload, run or locally download the repository and execute:

```bash
python verify_repository.py
```
