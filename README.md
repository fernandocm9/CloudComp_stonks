# CloudComp_stonks

This README file goes over the process of building and running the Stonks App on a cloud environment.

Clound Environments
1. Open up your Cloud Management Console create and deploy a virtual machine.
2. In the network configuration, select a port you want to open which will be used to serve the application.
3. Take not of the IP address that has been assigned to your virtual environment.
4.Connect to your virtual machine via SSH or Bastion
5. Type in the command "source venv/bin/activate" to activate the virtual environment.
6. Type in the "pwd" command to confirm you are in the root directory and can see the venv, application and templates directories.
7. Type in the command "flask run --host 0.0.0.0" to run the application on any IP address that can reach this machine. In this case it will be the IP address of your clound environment.
8. Enter the IP address of your cloud server and the port you configured open in another browser window to display the application.
9. Enter the stock and timeline you want to serach for and click on "Submit".
10. In the URL bar, add the "/chart" route to the end of your application address to display the chart.
11. This will display the chart for the stock and timeline you specified.
12. To terminate the application, heead back to your terminal window and enter "Ctrl + C" to end the connection.
