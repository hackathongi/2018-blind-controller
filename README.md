A Hackathon project to control the blinders of a House

# Resource

IP: 192.168.4.13
PORT: 80

## Vars

- `state`: defines de current state
  - `stopped`
  - `opening`
  - `closing`

- `percentage`: an integer that describes the opening %
  - `0`, `1`, ..., `100`
  
- `action`: ask the controller to trigger an action
  - `open`
  - `close`
  - `stop`
  
- `mode`: activates or not the automatic mode
  - `automatic`: blind behaviour is controlled by other sensors 
  - `manual`: behaviour is controlled manually


# Entity creation

MY_ENTITY="persiana"
MY_TYPE="blind_controller"

curl $ORION_SERVER:$ORION_PORT/v2/entities \
   -X POST -s -S --header  'Content-Type: application/json' -d @- <<EOF
{
  "id": "$MY_ENTITY",
  "type": "$MY_TYPE",
  "description": {
    "value": "Blind controller",
    "type": "String"
  },
  "state": {
    "value": "stopped",
    "type": "String"
  },
  "percentage": {
    "value": "100",
    "type": "String"
  },
  "action": {
    "value": "action",
    "type": "String"
  },
  "mode": {
    "value": "manual",
    "type": "String"
  }
}
EOF
