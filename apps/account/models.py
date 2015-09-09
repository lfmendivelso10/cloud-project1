from django.db import models

''' Represents Entidad que comparte los atributos de Agent y Client '''
class User(models.Model):
    first_name = models.CharField("first name", max_length=100)
    last_name = models.CharField("last name", max_length=100)
    email = models.CharField("email", max_length=100)
    password = models.CharField("password", max_length=20)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["last_name", "first_name"]

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)


''' Represents Entidad Administradores de la empresa    '''
class Agent(User):
    organization = models.CharField("organization", max_length=100)

    class Meta:
        verbose_name = "agent"
        verbose_name_plural = "agents"
        ordering = ["organization", "last_name", "first_name"]

    def __init__(self, organization, first_name, last_name, email, password):
        User.__init__(self, first_name, last_name, email, password)
        self.organization = organization


''' Represents Entidad de Concursos '''
class Contest(models.Model):
    agent =  models.ForeignKey(Agent, verbose_name="agent", related_name="contests")
    name = models.CharField("name", max_length=100)
    image = models.CharField("image banner", max_length=250)
    access_url = models.CharField("access URL", max_length=250)
    start_date = models.DateTimeField("start date", auto_now_add=True)
    end_date = models.DateTimeField("end date", auto_now_add=True)
    prize_description = models.CharField("prize description", max_length=250)

    class Meta:
        verbose_name = "contest"
        verbose_name_plural = "contests"
        ordering = ["start_date", "name"]

    def __unicode__(self):
        return self.name


''' Represents Entidad de Usuarios de la empresa    '''
class Client(User):
    contest =  models.ForeignKey(Contest, verbose_name="contest", related_name="clients")

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __init__(self, first_name, last_name, email, password):
        User.__init__(self, first_name, last_name, email, password)


''' Represents Entidad de Videos    '''
class Video(models.Model):
    owner =  models.ForeignKey(Client, verbose_name="owner", related_name="videos")
    description = models.CharField("description", max_length=250)
    original_url = models.CharField("original url", max_length=250)
    converted_url = models.CharField("converted url", max_length=250)
    status = models.CharField("status", max_length=250)

    class Meta:
        verbose_name = "contest"
        verbose_name_plural = "contests"
        ordering = ["start_date", "name"]

    def __unicode__(self):
        return "%s %s" % (self.original_url, self.status)