import os, subprocess, base64, webbrowser;

def die_python_die(error, msg, verbosity=-2):
	'''Throws exception with helpful error message and numeric exit code available to the shell'''
	try:
		raise Exception(msg)
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_exc(file=sys.stderr)
		sys.exit(error)

secret_sauce = 1 #set to zero to disable fixing the HTML and adding transcript download
inform7_project = "Edgecase Parchment"

compiler_inform7= "C:\\Program Files (x86)\\Inform 7\\Compilers\\ni"
compiler_inform6= "C:\\Program Files (x86)\\Inform 7\\Compilers\\inform6"
compiler_cblorb=  "C:\\Program Files (x86)\\Inform 7\\Compilers\\cblorb"

internal = "C:\\Program Files (x86)\\Inform 7\\Internal"
materials_dir = f"{os.getcwd()}"
inform_dir = f"{os.getcwd()}\\..\\{inform7_project}.inform"
build_dir = f"{inform_dir}\\Build"


os.chdir(materials_dir);
cmd = f"\"{compiler_inform7}\" -release -internal \"{internal}\" -project \"{inform_dir}\" -format=z8"

result = subprocess.Popen(cmd)
output = result.communicate()[0]
return_code = result.returncode
print(output)
print(f"Return code: {return_code}")
if (return_code != 0):
	die_python_die(return_code,"Inform 7 compile failed.")	

os.chdir(build_dir);
cmd = f"\"{compiler_inform6}\" -w~S~Dv8 +include_path=..\\Source,.\\ auto.inf output.z8"
result = subprocess.Popen(cmd)
output = result.communicate()[0]
return_code = result.returncode
print(output)
print(f"Return code: {return_code}")
if (return_code != 0):
	die_python_die(return_code,"Inform 6 compile failed.")

os.chdir(inform_dir);
cmd = f"\"{compiler_cblorb}\" -windows Release.blurb Build\output.zblorb"
result = subprocess.Popen(cmd)
output = result.communicate()[0]
return_code = result.returncode
print(output)
print(f"Return code: {return_code}")
if (return_code != 0):
	die_python_die(return_code,"Blorb compile failed.")

blorbdata = open(f"{build_dir}\\output.zblorb", "rb").read()
blorbstring = base64.b64encode(blorbdata).decode("utf-8")

dump = f"processBase64Zcode('{blorbstring}');";

f = open(f"{materials_dir}\\Release\\interpreter\\{inform7_project}.zblorb.js", "w")
f.write(dump)
f.close()

if (secret_sauce == 1):
	os.remove(f"{materials_dir}\\Release\\index.html")
	playcode = open(f"{materials_dir}\\Release\\play.html", "r").read();
	playcode = playcode.replace("<a href=\"index.html\">Home page</a>", "<input type='button' value='Download Transcript' onclick='downloadTranscript();'>")
	f = open(f"{materials_dir}\\Release\\play.html", "w")
	f.write(playcode)
	f.close()
	
webbrowser.open('file://' + os.path.realpath(f"{materials_dir}\\Release\\play.html"))