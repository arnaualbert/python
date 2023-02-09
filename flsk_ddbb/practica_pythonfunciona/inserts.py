# import the sqlite3 module
import sqlite3

# Define connection and cursor
connection = sqlite3.connect('database.db')
conn = connection.cursor()

# Insert data into the table

nameuno: str = "curry"

historiauno: str = "celebrando un triple"

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nameuno,historiauno)) # insert data in sqlite3 table

named: str = "messi"

hid: str = "messi la camiseta en el bernabeu"

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)", (named,hid)) # insert data in sqlite3 table

nt: str = "palou"

hit: str = "recien ganar la indy"
 
conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nt,hit)) # insert data in sqlite3 table

nq : str = "msn"

hiq: str ="messi ney y suarez"

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nq,hiq)) # insert data in sqlite3 table

nc: str = "bolt"

hic: str = "recien ganar un oro olimpico"

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nc,hic)) # insert data in sqlite3 table

ns: str = "motogp"

his: str ="carrera en assen ganada por Quartararo"

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(ns,his)) # insert data in sqlite3 table

#insert music data

namesit: str = "travis"

historiasit: str = "Jacques Berman Webster II, conocido bajo el nombre artístico de Travis Scott, es un rapero, compositor y productor musical estadounidense."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(namesit,historiasit))  # insert data in sqlite3 table

nameo: str = "mozart"

hio: str = "fue un compositor, pianista, director de orquesta y profesor del antiguo Arzobispado de Salzburgo, maestro del Clasicismo, considerado como uno de los músicos más influyentes y destacados de la historia"

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)", (nameo,hio)) # insert data in sqlite3 table

nn: str = "acdc"

hin: str = " es una banda de hard rock británica-australiana, formada en 1973 en Australia por los hermanos escoceses Malcolm Young y Angus Young."
 
conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nn,hin)) # insert data in sqlite3 table

marley: str = "marley"

hmarley: str  ="fue un cantante y compositor jamaicano. Durante su carrera musical fue el líder, compositor y guitarrista de las bandas The Wailers y Bob Marley & The Wailers."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(marley,hmarley)) # insert data in sqlite3 table

nb: str = "beatles"

hb: str = "fue una banda de rock británica formada en Liverpool durante los años 1960, estando integrada desde 1962 a su separación en 1970 por John Lennon, Paul McCartney, George Harrison y Ringo Starr."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nb,hb)) # insert data in sqlite3 table

sinatra: str = "sinatra"

hisin: str ="fue un cantante y actor estadounidense, considerado una de las figuras más importantes del siglo XX y uno de los cantantes más populares de todos los tiempos en Estados Unidos."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(sinatra,hisin)) # insert data in sqlite3 table


# insert ciencia
erwin: str = "erwin"

herwin: str = "La teoría predominante, llamada interpretación de Copenhague dice que un sistema cuántico permanece en superposición hasta que interactúa con el mundo externo o es observado por él. Cuando esto sucede, la superposición colapsa en uno u otro de los posibles estados definidos."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(erwin,herwin)) # insert data in sqlite3 table

marie: str = "marie"

hmarie: str = "Marie compensaba la carga del electrómetro con un cuarzo piezoeléctrico que ella hacía que se deformara para que produjera una corriente opuesta a la generada por los rayos, hasta conseguir que la aguja volviera a su posición inicial."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)", (marie,hmarie)) # insert data in sqlite3 table

newton: str = "newton"

hnewton: str = "Fue venerado durante su vida, descubrió las leyes de la gravedad y del movimiento, inventó el cálculo infinitesimal y ayudó a moldear nuestra visión racional del mundo."
 
conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(newton,hnewton)) # insert data in sqlite3 table

einstein: str = "einstein"

heinstein : str ="En 1905, cuando era un joven físico desconocido, empleado en la Oficina de Patentes de Berna, publicó su teoría de la relatividad especial. En ella incorporó, en un marco teórico simple fundamentado en postulados físicos sencillos, conceptos y fenómenos estudiados antes por Henri Poincaré y Hendrik Lorentz."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(einstein,heinstein)) # insert data in sqlite3 table

nobel: str = "nobel"

hnobel: str = "El ingeniero y empresario Alfred Nobel, inventor de la dinamita y fundador de los Premios Nobel. Alfred Nobel (1833-1896) creó los galardones que llevan su nombre para reconocer grandes descubrimientos que se hicieran cada año en beneficio de la humanidad."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(nobel,hnobel)) # insert data in sqlite3 table

franklin: str = "franklin"

hfranklin: str =" su célebre experimento de la cometa, demostró que la energía de las tormentas y la de las botellas de Leyden eran la misma cosa, instaurando así la ciencia de la electricidad."

conn.execute("INSERT INTO infofotos (name,historia) VALUES (?,?)",(franklin,hfranklin)) # insert data in sqlite3 table

# printing the cursor data
if conn:
	print("Data Inserted !")
else:
	print("Data Insertion Failed !")

# Commit the changes in database and Close the connection
connection.commit()
connection.close()
