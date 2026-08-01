# Section 1 → Section 2 reproducibility workflow

## Exact manuscript snapshot

1. Run the Section 1 notebook with `RUN_MODE = "MANUSCRIPT_SNAPSHOT"`.
2. Confirm `PIPELINE_SUCCESS.txt` and the Section 1 audit checks.
3. Download `Mushroom_KG_Reproducibility_Inputs_v2_from_upstream.zip`.
4. Open the Section 2 notebook:
   https://github.com/romenmeitei/AISKG_02_Framework
5. Upload the Section 1 bridge ZIP when prompted, or use the frozen Section 2
   companion ZIP already supplied in that repository.
6. Confirm the 94 fixed-result checks and `PIPELINE_SUCCESS.txt`.

The Section 1 bridge ZIP and the Section 2 frozen companion ZIP are intended to
produce the same manuscript-facing results. Section 2 locates the input
checksum manifest recursively after extraction.

## Optional live refresh

A live Section 1 run creates a current corpus and requires a completed human
topic-review file before extraction. It is a new dated analysis and should not
overwrite the frozen manuscript snapshot.
