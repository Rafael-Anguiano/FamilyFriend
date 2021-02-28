from django.shortcuts import render
from django.http import Http404, HttpResponse
from Seniors.models import PACIENTE
from Seniors.models import RESPONSABLE
from Seniors.models import MEDICAMENTO
from Seniors.models import TIPOCONTACTO
from Seniors.models import CONTACTO
from Seniors.models import SINTOMA
from Seniors.models import ENFERMEDAD
from Seniors.models import ENFERMEDICA
from Seniors.models import RESPAC
from Seniors.models import EVALUACION
from Seniors.models import ORIENTACION
from Seniors.models import CUERPO
from Seniors.models import GENERAL
from Seniors.models import DOLOR
from Seniors.models import FUERZA
from Seniors.models import ROM
from Seniors.models import EXTREMIDAD
from django.template import Template, Context
from django.template.loader import get_template
import datetime
import json as json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def info(request):
    return render(request, 'templateS/general-info.html')

def index(request):
	
	ctx = {'salida':"Hola, como estas", 'objetoId':"12344556" , 'user':'guest', "video":True}
	
	return render(request, 'templateS/index.html', context=ctx)


@csrf_exempt
def alta(request):
	if request.POST:
		try:
			print("hola acaba de hacer un post")
			print(request.POST)
			patient_name = request.POST['patient_name']
			patient_last_name = request.POST['patient_last_name']
			patient_email = request.POST['patient_email']
			patient_password = request.POST['patient_password']
			patient_address = request.POST['patient_address']
			patient_instagram = request.POST['patient_instagram']
			patient_telegram = request.POST['patient_telegram']
			patient_sex = request.POST['patient_sex']
			patient_whatsapp = request.POST['patient_whatsapp']
			patient_phone = request.POST['patient_phone']
			patient_verification_period = request.POST['patient_verification_period']
			if patient_verification_period == '':
				patient_verification_period = datetime.now()
			

			p = PACIENTE()
			p.patient_name = patient_name
			p.patient_last_name = patient_last_name
			p.patient_email = patient_email
			p.patient_password = patient_password
			p.patient_instagram = patient_instagram
			p.patient_telegram = patient_telegram
			p.patient_address = patient_address
			p.patient_sex = patient_sex
			p.patient_whatsapp = patient_whatsapp
			p.patient_phone = patient_phone
			p.patient_verification_period = patient_verification_period
			p.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaResponsable(request):
	if request.POST:
		try:
			print(request.POST)
			family_name = request.POST['family_name']
			family_last_name = request.POST['family_last_name']
			family_email = request.POST['family_email']
			family_instagram = request.POST['family_instagram']
			family_telegram = request.POST['family_telegram']
			family_address = request.POST['family_address']
			family_whatsapp = request.POST['family_whatsapp']
			family_phone = request.POST['family_phone']

			r = RESPONSABLE()
			r.family_name = family_name
			r.family_last_name = family_last_name
			r.family_email = family_email
			r.family_instagram = family_instagram
			r.family_telegram = family_telegram
			r.family_address = family_address
			r.family_whatsapp = family_whatsapp
			r.family_phone = family_phone

			r.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaRespac(request):
	if request.POST:
		try:
			print(request.POST)
			pe = request.POST['patient_email']
			fe = request.POST['family_email']

			p = PACIENTE.objects.filter(patient_email = pe).distinct()
			res = RESPONSABLE.objects.filter(family_email = fe).distinct()

			print(p)
			rp = RESPAC()
			rp.idpaciente_id = p[0].id
			rp.idresponsable_id = res[0].id

			rp.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaMedicamento(request):
	if request.POST:
		try:
			print(request.POST)
			medicine_name = request.POST['medicine_name']
			medicine_quantity = request.POST['medicine_quantity']
			medicine_regularity = request.POST['medicine_regularity']

			m = MEDICAMENTO()
			m.medicine_name = medicine_name
			m.medicine_quantity = medicine_quantity
			m.medicine_regularity = medicine_regularity
			m.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)


@csrf_exempt
def altaTipocontacto(request):
	if request.POST:
		try:
			print(request.POST)
			contact_type = request.POST['contact_type']

			tc = TIPOCONTACTO()
			tc.contact_type = contact_type
			tc.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaContacto(request):
	if request.POST:
		try:
			print(request.POST)
			pe = request.POST['patient_email']
			ct = request.POST['contact_type']
			print(pe)
			p = PACIENTE.objects.filter(patient_email = pe).distinct()
			tc = TIPOCONTACTO.objects.filter(contact_type = ct).distinct()
			contact_name = request.POST['contact_name']
			contact_last_name = request.POST['contact_last_name']
			contact_email = request.POST['contact_email']
			contact_instagram = request.POST['contact_instagram']
			contact_telegram = request.POST['contact_telegram']
			contact_address = request.POST['contact_address']
			contact_whatsapp = request.POST['contact_whatsapp']
			contact_phone = request.POST['contact_phone']

			c = CONTACTO()
			c.idpaciente_id = p[0].id
			c.idtipocontacto_id = tc[0].id
			c.contact_name = contact_name
			c.contact_last_name = contact_last_name
			c.contact_email = contact_email
			c.contact_instagram = contact_instagram
			c.contact_telegram = contact_telegram
			c.contact_address = contact_address
			c.contact_whatsapp = contact_whatsapp
			c.contact_phone = contact_phone

			c.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaSintoma(request):
	if request.POST:
		try:
			print(request.POST)
			pe = request.POST['patient_email']
			p = PACIENTE.objects.filter(patient_email = pe).distinct()
			current_symptom = request.POST['current_symptoms']

			s = SINTOMA()
			s.idpaciente_id = p[0].id
			s.current_symptom = current_symptom

			s.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)


@csrf_exempt
def altaEnfermedad(request):
	if request.POST:
		try:
			print(request.POST)
			pe = request.POST['patient_email']
			p = PACIENTE.objects.filter(patient_email = pe).distinct()
			current_disease = request.POST['current_disease']

			e = ENFERMEDAD()
			e.idpaciente_id = p[0].id
			e.current_disease = current_disease

			e.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaEnfermedica(request):
	if request.POST:
		try:
			print(request.POST)
			cd = request.POST['current_disease']
			mn = request.POST['medicine_name']
			mq = request.POST['medicine_quantity']
			e = ENFERMEDAD.objects.filter(current_disease = cd).distinct()
			m = MEDICAMENTO.objects.filter(medicine_name = mn, medicine_quantity = mq).distinct()

			em = ENFERMEDICA()
			em.idenfermedad_id = e[0].id
			em.idmedicamento_id = m[0].id

			em.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaEvaluacion(request):
	if request.POST:
		try:
			print(request.POST)
			pe = request.POST['patient_email']
			p = PACIENTE.objects.filter(patient_email = pe).distinct()
			evaluation_cva = request.POST['evaluation_cva']
			evaluation_cardiac = request.POST['evaluation_cardiac']
			evaluation_asthma = request.POST['evaluation_asthma']
			evaluation_smoker = request.POST['evaluation_smoker']
			evaluation_elevated_cholesterol = request.POST['evaluation_elevated_cholesterol']
			evaluation_breast_feeding = request.POST['evaluation_breast_feeding']
			evaluation_substance_abuse = request.POST['evaluation_substance_abuse']
			evaluation_hypertension = request.POST['evaluation_hypertension']
			evaluation_dialysis = request.POST['evaluation_dialysis']
			evaluation_migraine = request.POST['evaluation_migraine']
			evaluation_thyroid = request.POST['evaluation_thyroid']
			evaluation_alcoholism = request.POST['evaluation_alcoholism']
			evaluation_cancer = request.POST['evaluation_cancer']
			evaluation_seizures = request.POST['evaluation_seizures']
			evaluation_copd = request.POST['evaluation_copd']
			evaluation_psych = request.POST['evaluation_psych']
			evaluation_genitourinary = request.POST['evaluation_genitourinary']
			evaluation_geriatric = request.POST['evaluation_geriatric']
			evaluation_gestational_age = request.POST['evaluation_gestational_age']

			ev = EVALUACION()
			ev.idpaciente_id = p[0].id
			ev.evaluation_cva = evaluation_cva
			ev.evaluation_cardiac = evaluation_cardiac
			ev.evaluation_asthma = evaluation_asthma
			ev.evaluation_smoker = evaluation_smoker
			ev.evaluation_elevated_cholesterol = evaluation_elevated_cholesterol
			ev.evaluation_breast_feeding = evaluation_breast_feeding
			ev.evaluation_substance_abuse = evaluation_substance_abuse
			ev.evaluation_hypertension = evaluation_hypertension
			ev.evaluation_dialysis = evaluation_dialysis
			ev.evaluation_migraine = evaluation_migraine
			ev.evaluation_thyroid = evaluation_thyroid
			ev.evaluation_alcoholism = evaluation_alcoholism
			ev.evaluation_cancer = evaluation_cancer
			ev.evaluation_seizures = evaluation_seizures
			ev.evaluation_copd = evaluation_copd
			ev.evaluation_psych = evaluation_psych
			ev.evaluation_genitourinary = evaluation_genitourinary
			ev.evaluation_geriatric = evaluation_geriatric
			ev.evaluation_gestational_age = evaluation_gestational_age

			ev.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaOrientacion(request):
	if request.POST:
		try:
			print(request.POST)
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_loc = request.POST['evaluation_loc']
			evaluation_person = request.POST['evaluation_person']
			evaluation_place = request.POST['evaluation_place']
			evaluation_time = request.POST['evaluation_time']
			evaluation_situation = request.POST['evaluation_situation']

			evor = ORIENTACION()
			
			evor.idevaluation_id = ev[0].id
			evor.evaluation_loc = evaluation_loc
			evor.evaluation_person = evaluation_person
			evor.evaluation_place = evaluation_place
			evor.evaluation_time = evaluation_time
			evor.evaluation_situation = evaluation_situation

			evor.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaCuerpo(request):
	if request.POST:
		try:
			print(request.POST)
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_hair = request.POST['evaluation_hair']
			evaluation_perla = request.POST['evaluation_perla']
			evaluation_nose = request.POST['evaluation_nose']
			evaluation_ears = request.POST['evaluation_ears']
			evaluation_mouth = request.POST['evaluation_mouth']
			evaluation_midline_tongue = request.POST['evaluation_midline_tongue']
			evaluation_moist = request.POST['evaluation_moist']
			evaluation_lesions = request.POST['evaluation_lesions']
			evaluation_dentitions = request.POST['evaluation_dentitions']
			evaluation_chest_symmetry = request.POST['evaluation_chest_symmetry']
			evaluation_skin_turgor = request.POST['evaluation_skin_turgor']
			evaluation_Ranterior = request.POST['evaluation_ranterior']
			evaluation_Rposterior = request.POST['evaluation_rposterior']
			evaluation_Rlateral = request.POST['evaluation_rlateral']
			evaluation_Abinspection = request.POST['evaluation_abinspection']
			evaluation_Abpalpation = request.POST['evaluation_abpalpation']
			evaluation_ruq = request.POST['evaluation_ruq']
			evaluation_rlq = request.POST['evaluation_rlq']
			evaluation_luq = request.POST['evaluation_luq']
			evaluation_llq = request.POST['evaluation_llq']
			evaluation_skin = request.POST['evaluation_skin']
			evaluation_skin_description = request.POST['evaluation_skin_description']

			cu = CUERPO()
			cu.idevaluation_id = ev[0].id
			cu.evaluation_hair = evaluation_hair
			cu.evaluation_perla = evaluation_perla
			cu.evaluation_nose = evaluation_nose
			cu.evaluation_ears = evaluation_ears
			cu.evaluation_mouth = evaluation_mouth
			cu.evaluation_midline_tongue = evaluation_midline_tongue
			cu.evaluation_moist = evaluation_moist
			cu.evaluation_lesions = evaluation_lesions
			cu.evaluation_dentitions = evaluation_dentitions
			cu.evaluation_chest_symmetry = evaluation_chest_symmetry
			cu.evaluation_skin_turgor = evaluation_skin_turgor
			cu.evaluation_Ranterior = evaluation_Ranterior
			cu.evaluation_Rposterior = evaluation_Rposterior
			cu.evaluation_Rlateral = evaluation_Rlateral
			cu.evaluation_Abinspection = evaluation_Abinspection
			cu.evaluation_Abpalpation = evaluation_Abpalpation
			cu.evaluation_ruq = evaluation_ruq
			cu.evaluation_rlq = evaluation_rlq
			cu.evaluation_luq = evaluation_luq
			cu.evaluation_llq = evaluation_llq
			cu.evaluation_skin = evaluation_skin
			cu.evaluation_skin_description = evaluation_skin_description

			cu.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaGeneral(request):
	if request.POST:
		try:
			print(request.POST)
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_temp = request.POST['evaluation_temp']
			evaluation_bp = request.POST['evaluation_bp']
			evaluation_pulseOx = request.POST['evaluation_pulseOx']
			evaluation_pulseR = request.POST['evaluation_pulseR']
			evaluation_carotid_pulse = request.POST['evaluation_carotid_pulse']
			evaluation_carotid_pulse_type = request.POST['evaluation_carotid_pulse_type']
			evaluation_apical_pulse = request.POST['evaluation_apical_pulse']
			evaluation_apical_pulse_type = request.POST['evaluation_apical_pulse_type']
			evaluation_weight = request.POST['evaluation_weight']
			evaluation_height = request.POST['evaluation_height']
			evaluation_bm = request.POST['evaluation_bm']
			evaluation_radial_pulseS = request.POST['evaluation_radial_pulseS']
			evaluation_radial_pulseI = request.POST['evaluation_radial_pulseI']
			evaluation_fr_pulse = request.POST['evaluation_fr_pulse']
			evaluation_fl_pulse = request.POST['evaluation_fl_pulse']

			g = GENERAL()
			g.idevaluation_id = ev[0].id
			g.evaluation_temp = evaluation_temp
			g.evaluation_bp = evaluation_bp
			g.evaluation_pulseOx = evaluation_pulseOx
			g.evaluation_pulseR = evaluation_pulseR
			g.evaluation_carotid_pulse = evaluation_carotid_pulse
			g.evaluation_carotid_pulse_type = evaluation_carotid_pulse_type
			g.evaluation_apical_pulse = evaluation_apical_pulse
			g.evaluation_apical_pulse_type = evaluation_apical_pulse_type
			g.evaluation_weight = evaluation_weight
			g.evaluation_height = evaluation_height
			g.evaluation_bm = evaluation_bm
			g.evaluation_radial_pulseS = evaluation_radial_pulseS
			g.evaluation_radial_pulseI = evaluation_radial_pulseI
			g.evaluation_fr_pulse = evaluation_fr_pulse
			g.evaluation_fl_pulse = evaluation_fl_pulse

			g.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaDolor(request):
	if request.POST:
		try:
			print(request.POST)
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_pain = request.POST['evaluation_pain']
			evaluation_pain_escale = request.POST['evaluation_pain_escale']
			evaluation_pain_location = request.POST['evaluation_pain_location']
			evaluation_pain_duration = request.POST['evaluation_pain_duration']
			evaluation_pain_characteristics = request.POST['evaluation_pain_characteristics']
			evaluation_pain_precipitation = request.POST['evaluation_pain_precipitation']
			evaluation_pain_frecuency = request.POST['evaluation_pain_frecuency']
			evaluation_pain_non_verbals = request.POST['evaluation_pain_non_verbals']
			evaluation_pain_relief_factors = request.POST['evaluation_pain_relief_factors']
			evaluation_pain_sleep = request.POST['evaluation_pain_sleep']

			dol = DOLOR()
			dol.idevaluation_id = ev[0].id
			dol.evaluation_pain = evaluation_pain
			dol.evaluation_pain_escale = evaluation_pain_escale
			dol.evaluation_pain_location = evaluation_pain_location
			dol.evaluation_pain_duration = evaluation_pain_duration
			dol.evaluation_pain_characteristics = evaluation_pain_characteristics
			dol.evaluation_pain_precipitation = evaluation_pain_precipitation
			dol.evaluation_pain_frecuency = evaluation_pain_frecuency
			dol.evaluation_pain_non_verbals = evaluation_pain_non_verbals
			dol.evaluation_pain_relief_factors = evaluation_pain_relief_factors
			dol.evaluation_pain_sleep = evaluation_pain_sleep

			dol.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaFuerza(request):
	if request.POST:
		try:
			print(request.POST)
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_sur = request.POST['evaluation_sur']
			evaluation_sul = request.POST['evaluation_sul']
			evaluation_slr = request.POST['evaluation_slr']
			evaluation_sll = request.POST['evaluation_sll']
			evaluation_sensations = request.POST['evaluation_sensations']

			fu = FUERZA()
			fu.idevaluation_id = ev[0].id
			fu.evaluation_sur = evaluation_sur
			fu.evaluation_sul = evaluation_sul
			fu.evaluation_slr = evaluation_slr
			fu.evaluation_sll = evaluation_sll
			fu.evaluation_sensations = evaluation_sensations

			fu.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaROM(request):
	if request.POST:
		try:
			print(request.POST) 
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_rom_ur = request.POST['evaluation_rom_ur']
			evaluation_rom_ul = request.POST['evaluation_rom_ul']
			evaluation_rom_lr = request.POST['evaluation_rom_lr']
			evaluation_rom_ll = request.POST['evaluation_rom_ll']

			rom = ROM()
			rom.idevaluation_id = ev[0].id
			rom.evaluation_rom_ur = evaluation_rom_ur
			rom.evaluation_rom_ul = evaluation_rom_ul
			rom.evaluation_rom_lr = evaluation_rom_lr
			rom.evaluation_rom_ll = evaluation_rom_ll

			rom.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def altaExtremidad(request):
	if request.POST:
		try:
			print(request.POST)
			ep = request.POST['evaluation_psych']
			ev = EVALUACION.objects.filter(evaluation_psych = ep).distinct()
			evaluation_grip_sup = request.POST['evaluation_grip_sup']
			evaluation_veins_sup = request.POST['evaluation_veins_sup']
			evaluation_temp_vs_trunk_sup = request.POST['evaluation_temp_vs_trunk_sup']
			evaluation_capillary_refill = request.POST['evaluation_capillary_refill']
			evaluation_hair_present = request.POST['evaluation_hair_present']
			evaluation_foot_strength = request.POST['evaluation_foot_strength']
			evaluation_nails = request.POST['evaluation_nails']
			evaluation_nails_yellowed = request.POST['evaluation_nails_yellowed']
			evaluation_nails_thickened = request.POST['evaluation_nails_thickened']
			evaluation_nails_ingrown = request.POST['evaluation_nails_ingrown']
			evaluation_grip_low = request.POST['evaluation_grip_low']
			evaluation_veins_low = request.POST['evaluation_veins_low']
			evaluation_edema = request.POST['evaluation_edema']
			evaluation_homains = request.POST['evaluation_homains']
			evaluation_claudations = request.POST['evaluation_claudations']
			evaluation_temp_vs_trunk_low = request.POST['evaluation_temp_vs_trunk_low']

			ex = EXTREMIDAD()
			ex.idevaluation_id = ev[0].id
			ex.evaluation_grip_sup = evaluation_grip_sup
			ex.evaluation_veins_sup = evaluation_veins_sup
			ex.evaluation_temp_vs_trunk_sup = evaluation_temp_vs_trunk_sup
			ex.evaluation_capillary_refill = evaluation_capillary_refill
			ex.evaluation_hair_present = evaluation_hair_present
			ex.evaluation_foot_strength = evaluation_foot_strength
			ex.evaluation_nails = evaluation_nails
			ex.evaluation_nails_yellowed = evaluation_nails_yellowed
			ex.evaluation_nails_thickened = evaluation_nails_thickened
			ex.evaluation_nails_ingrown = evaluation_nails_ingrown
			ex.evaluation_grip_low = evaluation_grip_low
			ex.evaluation_veins_low = evaluation_veins_low
			ex.evaluation_edema = evaluation_edema
			ex.evaluation_homains = evaluation_homains
			ex.evaluation_claudations = evaluation_claudations
			ex.evaluation_temp_vs_trunk_low = evaluation_temp_vs_trunk_low

			ex.save()
			print("Se terminó")
			return HttpResponse("/")
		except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def baja(request):
	try:
		pe = request.POST['patient_email']
		pp = request.POST['patient_password']
		p = PACIENTE.objects.filter(patient_email = pe, patient_password = pp).distinct()

		if (len(p) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":p}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaResponsable(request):
	try:
		rd = request.POST['id']
		r = RESPONSABLE.objects.filter(id = rd).distinct()

		if (len(r) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":r}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaMedicamento(request):
	try:
		md = request.POST['id']
		m = MEDICAMENTO.objects.filter(id = md).distinct()

		if (len(m) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":m}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaContacto(request):
	try:
		cd = request.POST['id']
		c = CONTACTO.objects.filter(id = cd).distinct()
		ct = TIPOCONTACTO.objects.filter(id = cd).distinct()
		c.update(ct)
		
		if (len(c) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida": c}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaSintoma(request):
	try:
		sd = request.POST['id']
		s = SINTOMA.objects.filter(id = sd).distinct()

		if (len(s) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":s}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaEnfermedad(request):
	try:
		ed = request.POST['id']
		en = ENFERMEDAD.objects.filter(id = ed).distinct()

		if (len(en) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":en}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaEvaluacion(request):
	try:
		ed = request.POST['id']
		ev = EVALUACION.objects.filter(id = ed).distinct()

		if (len(ev) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":ev}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaOrientacion(request):
	try:
		od = request.POST['id']
		o = ORIENTACION.objects.filter(id = od).distinct()

		if (len(o) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":o}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaCuerpo(request):
	try:
		cd = request.POST['id']
		c = CUERPO.objects.filter(id = cd).distinct()

		if (len(c) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":c}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaGeneral(request):
	try:
		gd = request.POST['id']
		g = GENERAL.objects.filter(id = gd).distinct()

		if (len(g) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":g}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaDolor(request):
	try:
		dd = request.POST['id']
		d = DOLOR.objects.filter(id = dd).distinct()

		if (len(d) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":d}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaFuerza(request):
	try:
		fd = request.POST['id']
		f = FUERZA.objects.filter(id = fd).distinct()

		if (len(f) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":f}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaROM(request):
	try:
		rd = request.POST['id']
		rm = ROM.objects.filter(id = rd).distinct()

		if (len(rm) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":rm}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)

@csrf_exempt
def bajaExtremidad(request):
	try:
		exd = request.POST['id']
		ex = EXTREMIDAD.objects.filter(id = exd).distinct()

		if (len(ex) == 0):
			response = {"salida":"error"}
		else:
			response = {"salida":ex}

		return HttpResponse(json.dumps(response), content_type="aplication/json")

	except Exception as e:
			print("Ocurrio un error")
			print(e)