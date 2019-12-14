class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usernickname = models.CharField(db_column='userNickName', max_length=50, blank=True, null=True)
    userbirth = models.DateField(db_column='userBirth', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(instance)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()