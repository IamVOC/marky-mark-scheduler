from unittest.mock import Mock, patch, call
import datetime

from app.services.enqueuer_by_timetable_service import EnqueuerByTimetableService

def side_subgroup(value):
    dummy_db = {
            1400: [1, 2],
            1401: [2],
            1402: [1],
            }
    return dummy_db[value]

def side_group(value):
    dummy_db = {
            100: [1],
            101: [2, 3],
            102: [4, 5]
            }
    return dummy_db[value]

def side_get_group(value):

    group_100_mock = Mock()
    group_100_mock.json.return_value = [{'disciplineOid': 201, 'beginLesson': '13:15', 'subGroupOid': 0}, 
                                        {'disciplineOid': 202, 'beginLesson': '15:05', 'subGroupOid': 0}]
    group_101_mock = Mock()
    group_101_mock.json.return_value = [{'disciplineOid': 201, 'beginLesson': '14:45', 'subGroupOid': 0}]
    dummy_serv = {           
            'https://rasp.omgtu.ru/api/schedule/group/100?start=1900.01.01&finish=1900.01.01&lng=1': group_100_mock,
            'https://rasp.omgtu.ru/api/schedule/group/101?start=1900.01.01&finish=1900.01.01&lng=1': group_101_mock         
            }
    return dummy_serv[value]

def side_get_subgroup(value):

    group_100_mock = Mock()
    group_100_mock.json.return_value = [{'disciplineOid': 201, 'beginLesson': '13:15', 'subGroupOid': 1400}, 
                                        {'disciplineOid': 202, 'beginLesson': '15:05', 'subGroupOid': 1401}]
    group_101_mock = Mock()
    group_101_mock.json.return_value = [{'disciplineOid': 201, 'beginLesson': '14:45', 'subGroupOid': 1402}]
    dummy_serv = {           
            'https://rasp.omgtu.ru/api/schedule/group/100?start=1900.01.01&finish=1900.01.01&lng=1': group_100_mock,
            'https://rasp.omgtu.ru/api/schedule/group/101?start=1900.01.01&finish=1900.01.01&lng=1': group_101_mock         
            }
    return dummy_serv[value]

def side_get_banned(value):

    group_mock = Mock()
    group_mock.json.return_value = [{'disciplineOid': 200, 'beginLesson': '13:15', 'subGroupOid': 1400}]
    dummy_serv = {
                'https://rasp.omgtu.ru/api/schedule/group/100?start=1900.01.01&finish=1900.01.01&lng=1': group_mock,
                'https://rasp.omgtu.ru/api/schedule/group/101?start=1900.01.01&finish=1900.01.01&lng=1': group_mock
            }
    return dummy_serv[value]


requests_subjects_group_mock = Mock()
requests_subjects_group_mock.get.side_effect = side_get_group

requests_subjects_subgroup_mock = Mock()
requests_subjects_subgroup_mock.get.side_effect = side_get_subgroup

requests_subjects_banned_mock = Mock()
requests_subjects_banned_mock.get.side_effect = side_get_banned

date_mock = Mock()
date_mock.today.return_value = datetime.date(1900, 1, 1)
datetime_mock = Mock()
datetime_mock.return_value = datetime.time(12, 10, 0, 0)

task_group_mock = Mock()
task_subgroup_mock = Mock()
task_banned_mock = Mock()

groups_repo_mock = Mock()
groups_repo_mock_return = Mock()
groups_repo_mock_return.get_all_groups.return_value = [100, 101]
groups_repo_mock.return_value = groups_repo_mock_return

banned_subjects_repo = Mock()
banned_subjects_repo_return = Mock()
banned_subjects_repo_return.get_all_subjects.return_value = [200]
banned_subjects_repo.return_value = banned_subjects_repo_return

stud_subgroup_repo_mock = Mock()
stud_subgroup_repo_mock_return = Mock()
stud_subgroup_repo_mock_return.get_students_chatid_by_subgroup.side_effect = side_subgroup
stud_subgroup_repo_mock.return_value = stud_subgroup_repo_mock_return

stud_group_repo_mock = Mock()
stud_group_repo_mock_return = Mock()
stud_group_repo_mock_return.get_students_chatid_by_group.side_effect = side_group
stud_group_repo_mock.return_value = stud_group_repo_mock_return


@patch('app.utils.date', new=date_mock)
@patch('app.utils.get_current_time', new=datetime_mock)
@patch('app.services.enqueuer_by_timetable_service.GroupRepository', new=groups_repo_mock)
@patch('app.services.enqueuer_by_timetable_service.BannedSubjectsRepository', new=banned_subjects_repo)
@patch('app.services.enqueuer_by_timetable_service.StudentsSubgroupRepository', new=stud_subgroup_repo_mock)
@patch('app.services.enqueuer_by_timetable_service.StudentsGroupRepository', new=stud_group_repo_mock)
class TestEnqueuerService:
    
    @patch('app.services.enqueuer_by_timetable_service.send_notification', new=task_group_mock)
    @patch('app.services.enqueuer_by_timetable_service.requests', new=requests_subjects_group_mock)
    def test_service_get_by_group(self):
        service = EnqueuerByTimetableService()

        service.send_tasks_according_to_timetable()

        task_group_mock.apply_async.assert_has_calls([call(args=[1], countdown=3900),
                                                call(args=[1], countdown=10500),
                                                call(args=[2], countdown=9300),
                                                call(args=[3], countdown=9300)])

    @patch('app.services.enqueuer_by_timetable_service.send_notification', new=task_subgroup_mock)
    @patch('app.services.enqueuer_by_timetable_service.requests', new=requests_subjects_subgroup_mock)
    def test_service_get_by_subgroup(self):
        service = EnqueuerByTimetableService()

        service.send_tasks_according_to_timetable()

        task_subgroup_mock.apply_async.assert_has_calls([call(args=[1], countdown=3900),
                                                call(args=[2], countdown=3900),
                                                call(args=[2], countdown=10500),
                                                call(args=[1], countdown=9300)])

    @patch('app.services.enqueuer_by_timetable_service.send_notification', new=task_banned_mock)
    @patch('app.services.enqueuer_by_timetable_service.requests', new=requests_subjects_banned_mock)
    def test_service_get_banned(self):
        service = EnqueuerByTimetableService()

        service.send_tasks_according_to_timetable()

        task_banned_mock.apply_async.assert_not_called()    


