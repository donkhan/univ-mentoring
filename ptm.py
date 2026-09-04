import pandas as pd

courses = ["powerbi", "python"]
att_cutoff = [80, 80]
mark_cutoff = [7.5, 12.5]
for c in range(len(courses)):
    # Attendance
    attendance = pd.read_excel(
        courses[c] + "-attendence.xlsx",
        header=None
    )

    attendance = attendance[[1, 2, 20, 21]]
    attendance.columns = [
        "Register No",
        "Name",
        "Total Hour(s)",
        "Percentage"
    ]

    attendance["Percentage"] = (
        attendance["Percentage"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .astype(float)
    )


    # Assessment
    assessment = pd.read_excel(
        "powerbi-assessment.xlsx",
        header=None
    )

    assessment = assessment[[1, 2, 5]]
    assessment.columns = [
        "Register No",
        "Name",
        "Mid-Semester"
    ]


    # Merge
    result = pd.merge(
        attendance,
        assessment[["Register No", "Mid-Semester"]],
        on="Register No",
        how="inner"
    )


    # Filter
    shortlist = result[
        (result["Percentage"] < att_cutoff[c] ) |
        (result["Mid-Semester"].eq("AB")) |
        (pd.to_numeric(result["Mid-Semester"], errors="coerce") < mark_cutoff[c])
    ]

    print(shortlist)