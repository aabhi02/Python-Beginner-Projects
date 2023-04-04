import time
from plyer import notification


if __name__=="__main__":

		notification.notify(                   #type: ignore
			title = "HEADING HERE",
			message=" DESCRIPTION HERE" ,
		
			# displaying time
			timeout=2
)
		# waiting time
		time.sleep(7)
