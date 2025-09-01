DEFAULT_MOD_NAME = "Template"
class SearchFormat:
	IMAGE_FORMAT = "Image File (*.png);;Any file (*.*)"
	JSON_FORMAT = "Json File (*.json);;Any file (*.*)"
class Engine:
	PSYCH = 0
	CODENAME = 1
	VSLICE = 2
	@staticmethod
	def getName(id):
		match id:
			case Engine.PSYCH:
				return "PSYCH"
			case Engine.CODENAME:
				return "CODENAME"
			case Engine.VSLICE:
				return "VSLICE"
			case __:
				return "UNKNOWN"

class Character:
	DAD = 0
	BOYFRIEND = 1
	GF = 2
	@staticmethod
	def getName(id):
		match id:
			case Character.DAD:
				return "dad"
			case Character.BOYFRIEND:
				return "boyfriend"
			case Character.GF:
				return "gf"
			case __:
				return "unknown"
			
class Events:
	CAMERA_FOCUS = "(funkinTool)-camfocus"
	CHANGE_BPM = "(funkinTool)-bpmchange"
	PLAY_ANIMATION = "(funkinTool)-playanim"
	CHANGE_CHARACTER = "(funkinTool)-changecharacter"
	CHANGE_SCROLL_SPEED = "(funkinTool)-changescrollspeed"
	ADD_ZOOM = "(funkinTool)-addzoom"

class Notes:
	ALT_ANIM = "(funkinTool)-altanim"
	NO_ANIM = "(funkinTool)-noanim"
class Camera:
	HUD = "(funkinTool)-REFcamHUD"
	GAME = "(funkinTool)-REFcamGame"
