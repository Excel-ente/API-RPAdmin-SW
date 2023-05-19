# ----------------------------------------------------------
# Listas utilizadas por modelos de bases de datos
#
# Desarrollador: Kevin Turkienich - 2023
# ----------------------------------------------------------

# -- TIPO DE SERVIDOR -------------
TIPO_SERVER = [
    ("Desarrollo","Desarrollo"),
    ("Test","Test"),
    ("Produccion","Produccion"),
]
# -----------------------------------------

# -- VARIABLES CHOICES OPERATIVOS ---------
CHOICES_SO = [ 
    ("Windows","Windows"),
    ("Linux","Linux"),
    ("Mac","Mac"),
]
# -----------------------------------------

# -- ESTADOS DE INCIDENTES ----------------
ESTADO_INCIDENCIAS = [
    ("Recibido","Recibido"),
    ("En Proceso","En Proceso"),
    ("Finalizado","Finalizado"),
]
# -----------------------------------------

# -- ESTADOS DE TAREAS ----------------
ESTADO_TAREAS = [
    ("No inciado","No inciado"),
    ("inciado","inciado"),
    ("Esperando Respuesta","Esperando Respuesta"),
    ("Finalizada","Finalizada"),

]
# -----------------------------------------

# -- CHOICES SI/NO ------------------------

YES_NO = [
    ("SI","SI"),
    ("NO","NO"),
]
# -----------------------------------------

# -- CHOICES TIPO EJECUCION  --------------
at="at"
de="de"
TIPO_EJECUCION = [
    (at,"Atendido"),
    (de,"Desatendido"),
]
# -----------------------------------------

# -- CHOICES PERIODICIDAD  ----------------
PERIODICIDAD = [
    ("Diario","Diario"),
    ("Quincenal","Quincenal"),
    ("Mensual","Mensual"),
    ("Bimestral","Bimestral"),
    ("Trimestral","Trimestral"),
    ("Semestral","Semestral"),
    ("Anual","Anual"),
]
# -----------------------------------------

# -- CHOICES TIPO ESFUERZO  ---------------
TIPO_ESFUERZO = [
    ("Bajo","Bajo"),
    ("Medio","Medio"),
    ("Alto","Alto"),
]
# -----------------------------------------

# --- DIAS DE LA SEMANA  ------------------
DIAS = [
    ("Lunes","Lunes"),
    ("Martes","Martes"),
    ("Miercoles","Miercoles"),
    ("Jueves","Jueves"),
    ("Viernes","Viernes"),
    ("Sabado","Sabado"),
    ("Domingo","Domingo"),
]
# -----------------------------------------

# --- ESTADOS DE ROBOT  ------------------
ATENDIDO_DESATENDIDO = [
    ("Atendido","Atendido"),
    ("Desatendido","Desatendido"),
]
# -----------------------------------------
