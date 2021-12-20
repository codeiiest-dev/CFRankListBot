import requests

URL = "https://codeforces.com/api/contest.standings?contestId=CONTEST_ID&handles="


def format_name(name, handle):
    fname, lname = name.split(' ', 1)
    return '{fname} <a href="https://codeforces.com/profile/{handle}">{handle}</a> {lname}'.format(fname=fname, handle=handle, lname=lname)


def get_contest_data(contest_id, handles_str):
    """Get the contest data from Codeforces API."""
    url = URL.replace("CONTEST_ID", str(contest_id))
    url += handles_str
    response = requests.get(url)
    return response.json()


def filter_top_participants(contest_data, participants_info):
    """Filter the top participants."""
    participants = contest_data['result']['rows']

    overall = []
    top2ndYear = []
    top1stYear = []
    topFemales = []

    for participant in participants[:3]:
        handle = participant['party']['members'][0]['handle']
        overall.append(format_name(participants_info[handle]['name'], handle))

    for participant in participants:
        handle = participant['party']['members'][0]['handle']
        if participants_info[handle]['year'] == 2025:
            top1stYear.append(format_name(
                participants_info[handle]['name'], handle))
        elif participants_info[handle]['year'] == 2024:
            top2ndYear.append(format_name(
                participants_info[handle]['name'], handle))

    return {
        'overall': overall,
        'top2ndYear': top2ndYear[:3],
        'top1stYear': top1stYear[:3],
        'topFemales': topFemales[:3]
    }
