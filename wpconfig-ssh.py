import paramiko

# SSH connection details
hostname = 'example.com'
port = 22
username = 'your_username'
password = 'your_password'

# Path to the wp-config.php file on the server
remote_path = 'https://intervance.nl/wp-config.php'

# Define the desired permissions
desired_permissions = '777'  # Change this value as needed

# Establish SSH connection
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, port, username, password)

# Execute command to change permissions
command = f'chmod {desired_permissions} {remote_path}'
stdin, stdout, stderr = ssh_client.exec_command(command)

# Check for any errors
if stderr.channel.recv_exit_status() == 0:
    print(f"Permissions of {remote_path} changed to {desired_permissions}")
else:
    print("Error:", stderr.read().decode())

# Close SSH connection
ssh_client.close()