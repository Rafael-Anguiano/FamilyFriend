# -*- coding: cp1252 -*-
from django.db import models
from django.conf import settings
from django.utils import timezone




class identificador_user( models.Model ) :
	palabra=models.CharField( max_length=40 )
	def __unicode__(self):
		return '%s' % (self.palabra)

class Comment(models.Model):
	name = models.TextField(max_length=30)
	comment = models.TextField(max_length=300)
	def __unicode__(self):
		return self.name

class Stack(models.Model):
	IDE = models.TextField()
	last_seven_u = models.TextField()
	last_seven_r = models.TextField()
	def __unicode__(self):
		return '%s' %(self.last_seven_u)

class PeopleDic( models.Model ):
	All_Names = models.CharField(max_length=255)
	LetterLastName = models.CharField(max_length=1)
	Custom_Name = models.CharField(max_length=255)
	Custom_LastName = models.CharField(max_length=255)
	def __str__( self ):
		return '%s %s' % (self.Custom_LastName.encode('ascii', 'ignore'), self.Custom_Name.encode('ascii', 'ignore'), )

class NamesDic(models.Model):
	LetterName = models.CharField(max_length=1)
	Name = models.CharField(max_length=255)
	Genre = models.IntegerField(default=0)
	def __str__(self):
		return '%s %s' % (self.LetterName.encode('ascii', 'ignore'), self.Name.encode('ascii', 'ignore'),)

class AnaphoraOnOff(models.Model):
	on = models.BooleanField(default=False)
	IDE = models.TextField()
	def __unicode__(self):
		return '%s' % (self.on)

class UserRachael(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  def __unicode__(self):
        return '%s, %s' %(self.username, self.password)

# Base de datos grandes

# Create your models here.
class PACIENTE (models.Model):
	patient_name = models.CharField(max_length=30, default='No Def')
	patient_last_name = models.CharField(max_length=30, default='No Def')
	patient_email = models.CharField(max_length=30, default='No Def')
	patient_password = models.CharField(max_length=8)
	patient_instagram = models.CharField(max_length=30, default='No Def')
	patient_telegram = models.CharField(max_length=30, default='No Def')
	patient_address = models.CharField(max_length=30, default='No Def')
	patient_sex = models.CharField(max_length=30, default='No Def')
	patient_whatsapp = models.BigIntegerField(default=0)
	patient_phone = models.IntegerField(default=0)
	patient_verification_period = models.DateField(default = timezone.now)
	ordering = ('patient_name',)

	def __unicode__(self):
		return u'%s %s' % (self.patient_name.encode('ascii', 'ignore'), self.patient_last_name) 

class RESPONSABLE (models.Model):
	family_name = models.CharField(max_length=30, default='No Def')
	family_last_name = models.CharField(max_length=30, default='No Def')
	family_email = models.CharField(max_length=30, default='No Def')
	family_instagram = models.CharField(max_length=30, default='No Def')
	family_telegram = models.CharField(max_length=30, default='No Def')
	family_address = models.CharField(max_length=30, default='No Def')
	family_whatsapp = models.BigIntegerField(default=0)
	family_phone = models.IntegerField(default=0)
	ordering = ('family_name',)

	def __unicode__(self):
		return u'%s %s' % (self.family_name.encode('ascii', 'ignore'), self.family_last_name) 

class MEDICAMENTO (models.Model):
	medicine_name = models.CharField(max_length=30, default='No Def')
	medicine_quantity = models.CharField(max_length=30, default='No Def')
	medicine_regularity = models.CharField(max_length=30, default='No Def')
	ordering = ('medicine_name',)

	def __unicode__(self):
		return u'%s %s' % (self.medicine_name.encode('ascii', 'ignore'), self.medicine_quantity) 

class TIPOCONTACTO (models.Model):
	contact_type = models.CharField(max_length=30, default='No Def')
	ordering = ('contact_type',)

class CONTACTO (models.Model):
	idpaciente = models.ForeignKey(PACIENTE, on_delete = models.CASCADE)
	idtipocontacto = models.ForeignKey(TIPOCONTACTO, on_delete = models.CASCADE)
	contact_name = models.CharField(max_length=30, default='No Def')
	contact_last_name = models.CharField(max_length=30, default='No Def')
	contact_email = models.CharField(max_length=30, default='No Def')
	contact_instagram = models.CharField(max_length=30, default='No Def')
	contact_telegram = models.CharField(max_length=30, default='No Def')
	contact_address = models.CharField(max_length=30, default='No Def')
	contact_whatsapp = models.BigIntegerField(default=0)
	contact_phone = models.IntegerField(default=0)
	ordering = ('idpaciente',)

	def __unicode__(self):
		return u'%s %s' % (self.idpaciente.encode('ascii', 'ignore')) 

class SINTOMA (models.Model):
	idpaciente = models.ForeignKey(PACIENTE, on_delete = models.CASCADE)
	current_symptom = models.CharField(max_length=30, default='No Def')
	ordering = ('idpaciente',)

	def __unicode__(self):
		return u'%s %s' % (self.idpaciente.encode('ascii', 'ignore'), self.current_symptom) 



class ENFERMEDAD (models.Model):
	idpaciente = models.ForeignKey(PACIENTE,on_delete = models.CASCADE)
	current_disease = models.CharField(max_length=30, default='No Def')
	ordering = ('idpaciente',)

	def __unicode__(self):
		return u'%s %s' % (self.idpaciente.encode('ascii', 'ignore'), self.current_disease) 

class ENFERMEDICA (models.Model):
	idenfermedad = models.ForeignKey(ENFERMEDAD, on_delete = models.CASCADE)
	idmedicamento = models.ForeignKey(MEDICAMENTO, on_delete = models.CASCADE)
	ordering = ('idenfermedad',)

	def __unicode__(self):
		return u'%s %s' % (self.idenfermedad.encode('ascii', 'ignore'), self.idmedicamento) 

class RESPAC (models.Model):
	idpaciente = models.ForeignKey(PACIENTE, on_delete = models.CASCADE)
	idresponsable = models.ForeignKey(RESPONSABLE, on_delete = models.CASCADE)
	
	def __unicode__(self):
		return u'%s %s' % (self.idpaciente.encode('ascii', 'ignore'), self.idresponsable) 

class EVALUACION (models.Model):
	idpaciente = models.ForeignKey(PACIENTE, on_delete = models.CASCADE)
	evaluation_cva = models.BooleanField(default=False)
	evaluation_cardiac = models.BooleanField(default=False)
	evaluation_asthma = models.BooleanField(default=False)
	evaluation_smoker = models.BooleanField(default=False)
	evaluation_elevated_cholesterol = models.BooleanField(default=False)
	evaluation_breast_feeding = models.BooleanField(default=False)
	evaluation_substance_abuse = models.BooleanField(default=False)
	evaluation_hypertension = models.BooleanField(default=False)
	evaluation_dialysis = models.BooleanField(default=False)
	evaluation_migraine = models.BooleanField(default=False)
	evaluation_thyroid = models.BooleanField(default=False)
	evaluation_alcoholism = models.BooleanField(default=False)
	evaluation_cancer = models.BooleanField(default=False)
	evaluation_seizures = models.BooleanField(default=False)
	evaluation_copb = models.BooleanField(default=False)
	evaluation_psych = models.CharField(max_length=100, default='No Def')
	evaluation_genitourinary = models.CharField(max_length=100, default='No Def')
	evaluation_geriatric = models.CharField(max_length=100, default='No Def')
	evaluation_gestational_age = models.CharField(max_length=30, default='No Def')
	ordering = ('idpaciente',)

	def __unicode__(self):
		return u'%s %s' % (self.idpaciente.encode('ascii', 'ignore'), self.evaluation_cva) 

class ORIENTACION (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_loc = models.CharField(max_length=30, default='No Def')
	evaluation_person = models.CharField(max_length=30, default='No Def')
	evaluation_place = models.CharField(max_length=30, default='No Def')
	evaluation_time = models.CharField(max_length=30, default='No Def')
	evaluation_situation = models.CharField(max_length=30, default='No Def')
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_loc) 

class CUERPO (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_hair = models.CharField(max_length=30, default='No Def')
	evaluation_perla = models.CharField(max_length=30, default='No Def')
	evaluation_nose = models.CharField(max_length=30, default='No Def')
	evaluation_ears = models.CharField(max_length=30, default='No Def')
	evaluation_mouth = models.CharField(max_length=30, default='No Def')
	evaluation_midline_tongue = models.CharField(max_length=30, default='No Def')
	evaluation_moist = models.CharField(max_length=30, default='No Def')
	evaluation_lesions = models.CharField(max_length=30, default='No Def')
	evaluation_dentitions = models.CharField(max_length=30, default='No Def')
	evaluation_chest_symmetry = models.CharField(max_length=30, default='No Def')
	evaluation_skin_turgor = models.CharField(max_length=30, default='No Def')
	evaluation_Ranterior = models.CharField(max_length=30, default='No Def')
	evaluation_Rposterior = models.CharField(max_length=30, default='No Def')
	evaluation_Rlateral = models.CharField(max_length=30, default='No Def')
	evaluation_Abdinspection = models.CharField(max_length=30, default='No Def')
	evaluation_Abdpalpation = models.CharField(max_length=100, default='No Def')
	evaluation_ruq = models.CharField(max_length=30, default='No Def')
	evaluation_rlq = models.CharField(max_length=30, default='No Def')
	evaluation_luq = models.CharField(max_length=30, default='No Def')
	evaluation_llq = models.CharField(max_length=30, default='No Def')
	evaluation_skin = models.CharField(max_length=30, default='No Def')
	evaluation_skin_description = models.CharField(max_length=30, default='No Def')
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_hair) 

class GENERAL (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_temp = models.IntegerField(default=0)
	evaluation_bp = models.CharField(max_length=30, default='No Def')
	evaluation_pulseOx = models.IntegerField(default=0)
	evaluation_pulseR = models.IntegerField(default=0)
	evaluation_carotid_pulse = models.IntegerField(default=0)
	evaluation_carotid_pulse_type = models.CharField(max_length=30, default='No Def')
	evaluation_apical_pulse = models.IntegerField(default=0)
	evaluation_apical_pulse_type = models.CharField(max_length=30, default='No Def')
	evaluation_weight = models.CharField(max_length=30, default='No Def')
	evaluation_height = models.CharField(max_length=30, default='No Def')
	evaluation_bm = models.CharField(max_length=30, default='No Def')
	evaluation_radial_pulseS = models.IntegerField(default=0)
	evaluation_radial_pulseI = models.IntegerField(default=0)
	evaluation_fr_pulse = models.IntegerField(default=0)
	evaluation_fl_pulse = models.IntegerField(default=0)
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_temp) 

class DOLOR (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_pain = models.CharField(max_length=30, default='No Def')
	evaluation_pain_escale = models.CharField(max_length=30, default='No Def')
	evaluation_pain_location = models.CharField(max_length=30, default='No Def')
	evaluation_pain_duration = models.CharField(max_length=30, default='No Def')
	evaluation_pain_characteristics = models.CharField(max_length=30, default='No Def')
	evaluation_pain_precipitation = models.CharField(max_length=30, default='No Def')
	evaluation_pain_frecuency = models.CharField(max_length=30, default='No Def')
	evaluation_pain_non_verbals = models.CharField(max_length=30, default='No Def')
	evaluation_pain_relief_factors = models.CharField(max_length=30, default='No Def')
	evaluation_pain_sleep = models.CharField(max_length=30, default='No Def')
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_pain) 

class FUERZA (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_sur = models.CharField(max_length=30, default='No Def')
	evaluation_sul = models.CharField(max_length=30, default='No Def')
	evaluation_slr = models.CharField(max_length=30, default='No Def')
	evaluation_sll = models.CharField(max_length=30, default='No Def')
	evaluation_sensations = models.CharField(max_length=30, default='No Def')
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_sur) 

class ROM (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_rom_ur = models.CharField(max_length=30, default='No Def')
	evaluation_rom_ul = models.CharField(max_length=30, default='No Def')
	evaluation_rom_lr = models.CharField(max_length=30, default='No Def')
	evaluation_rom_ll = models.CharField(max_length=30, default='No Def')
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_rom_ur) 

class EXTREMIDAD (models.Model):
	idevaluation = models.ForeignKey(EVALUACION, on_delete = models.CASCADE)
	evaluation_grip_sup = models.CharField(max_length=30, default='No Def')
	evaluation_veins_sup = models.CharField(max_length=30, default='No Def')
	evaluation_temp_vs_trunk_sup = models.CharField(max_length=30, default='No Def')
	evaluation_capillary_refill = models.BooleanField(default=False)
	evaluation_hair_present = models.BooleanField(default=False)
	evaluation_foot_strength = models.BooleanField(default=False)
	evaluation_nails = models.BooleanField(default=False)
	evaluation_nails_yellowed = models.BooleanField(default=False)
	evaluation_nails_thickened = models.BooleanField(default=False)
	evaluation_nails_ingrown = models.BooleanField(default=False)
	evaluation_grip_low = models.CharField(max_length=30, default='No Def')
	evaluation_veins_low = models.CharField(max_length=30, default='No Def')
	evaluation_edema = models.CharField(max_length=30, default='No Def')
	evaluation_homains = models.CharField(max_length=30, default='No Def')
	evaluation_claudations = models.CharField(max_length=30, default='No Def')
	evaluation_temp_vs_trunk_low = models.CharField(max_length=30, default='No Def')
	ordering = ('idevaluation',)

	def __unicode__(self):
		return u'%s %s' % (self.idevaluation.encode('ascii', 'ignore'), self.evaluation_grip_sup)






