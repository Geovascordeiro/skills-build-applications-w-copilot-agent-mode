from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Activities
        Activity.objects.create(user=tony.email, type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=steve.email, type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=bruce.email, type='swim', duration=25, date='2023-01-03')
        Activity.objects.create(user=clark.email, type='run', duration=60, date='2023-01-04')

        # Workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='easy')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
