# Select all female bears and return their names and ages
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# Select bears that are alive and have a temperament of 'Friendly' or 'Calm'
select_friendly_or_calm_alive_bears = """
    SELECT
        name,
        temperament
    FROM bears
    WHERE alive = 1
    AND (temperament = 'Friendly' OR temperament = 'Calm');
"""

# Select the oldest bear
select_oldest_bear = """
    SELECT
        name,
        MAX(age) AS age
    FROM bears;
"""

# Select the count of male bears
select_count_of_male_bears = """
    SELECT
        COUNT(*) AS male_bear_count
    FROM bears
    WHERE sex = 'M';
"""

sys.path.append('/home/kevin/python-p3-organizing-bears-lab')

