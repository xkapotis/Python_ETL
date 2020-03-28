import pandas as pd

############### Your Queries with your databases ##################

def queries(source_cnxn, target_cursor_cnxn):

    #######################################
            # courses
    #######################################
    extract_courses = '''
    SELECT idCourses, Title
    FROM dbo.Courses
    '''

    df = pd.io.sql.read_sql(extract_courses, source_cnxn)
    df["Title"] = df["Title"].apply(lambda x: x[:39])
    x = df.values.tolist()

    insert_courses = '''
    INSERT INTO course (course_id, title)
    VALUES (?, ?);'''

    for row in x:
        target_cursor_cnxn.execute(insert_courses, (row[0], row[1]))
    target_cursor_cnxn.commit()
    #######################################
            # courses
    #######################################


    #######################################
            # members
    #######################################
    extract_members = '''
    SELECT idMembers, Name, sName
    FROM dbo.Members
    '''
    df_members = pd.io.sql.read_sql(extract_members, source_cnxn)
    df_members["Name"] = df_members["Name"].apply(lambda x: x[:39])
    df_members["sName"] = df_members["sName"].apply(lambda x: x[:39])
    x_members = df_members.values.tolist()

    insert_members = '''
    INSERT INTO student (student_id, first_name, last_name)
    VALUES (?, ?, ?);'''
    for row in x_members:
        target_cursor_cnxn.execute(insert_members, (row[0], row[1], row[2]))
    target_cursor_cnxn.commit()
    #######################################
            # members
    #######################################





