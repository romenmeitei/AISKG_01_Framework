# Public-release checklist — Section 1

- [ ] Delete obsolete files from the current repository:
  `CITATION.cff.template`, `GITHUB_ROOT_README.md`,
  `LICENSE_SELECTION_REQUIRED.md`, and `REPOSITORY_TEST_STATUS.md`.
- [ ] Upload every file and preserve `queries/`, `reference_outputs/`, and
  `.github/workflows/`.
- [ ] Confirm the Colab badge opens the current repository notebook.
- [ ] Run `python verify_repository.py`.
- [ ] Run the notebook in `MANUSCRIPT_SNAPSHOT` mode and confirm success.
- [ ] Review `THIRD_PARTY_DATA_NOTICE.md` with the institution before leaving
  the frozen bibliographic snapshot public.
- [ ] Confirm the copyright statement is compatible with institutional and
  contributor agreements.
- [ ] Create GitHub release `v1.0.0` and archive it with a DOI.
- [ ] Add the DOI to `CITATION.cff` and the manuscript.
