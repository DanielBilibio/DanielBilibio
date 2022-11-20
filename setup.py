import cx_Freeze

executables = [cx_Freeze.Executable(
    script="pistacarro.py",
)]
cx_Freeze.setup(
    name="pistacarro",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)
