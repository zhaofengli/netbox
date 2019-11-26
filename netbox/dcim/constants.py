from .choices import InterfaceTypeChoices


#
# Interface type groups
#

VIRTUAL_IFACE_TYPES = [
    InterfaceTypeChoices.TYPE_VIRTUAL,
    InterfaceTypeChoices.TYPE_LAG,
]

WIRELESS_IFACE_TYPES = [
    InterfaceTypeChoices.TYPE_80211A,
    InterfaceTypeChoices.TYPE_80211G,
    InterfaceTypeChoices.TYPE_80211N,
    InterfaceTypeChoices.TYPE_80211AC,
    InterfaceTypeChoices.TYPE_80211AD,
]

NONCONNECTABLE_IFACE_TYPES = VIRTUAL_IFACE_TYPES + WIRELESS_IFACE_TYPES

# Bootstrap CSS classes for device/rack statuses
STATUS_CLASSES = {
    0: 'warning',
    1: 'success',
    2: 'info',
    3: 'primary',
    4: 'danger',
    5: 'default',
    6: 'warning',
}

# Console/power/interface connection statuses
CONNECTION_STATUS_PLANNED = False
CONNECTION_STATUS_CONNECTED = True
CONNECTION_STATUS_CHOICES = [
    [CONNECTION_STATUS_PLANNED, 'Planned'],
    [CONNECTION_STATUS_CONNECTED, 'Connected'],
]

# Cable endpoint types
CABLE_TERMINATION_TYPES = [
    'consoleport', 'consoleserverport', 'interface', 'poweroutlet', 'powerport', 'frontport', 'rearport',
    'circuittermination',
]

CABLE_TERMINATION_TYPE_CHOICES = {
    # (API endpoint, human-friendly name)
    'consoleport': ('console-ports', 'Console port'),
    'consoleserverport': ('console-server-ports', 'Console server port'),
    'powerport': ('power-ports', 'Power port'),
    'poweroutlet': ('power-outlets', 'Power outlet'),
    'interface': ('interfaces', 'Interface'),
    'frontport': ('front-ports', 'Front panel port'),
    'rearport': ('rear-ports', 'Rear panel port'),
}

COMPATIBLE_TERMINATION_TYPES = {
    'consoleport': ['consoleserverport', 'frontport', 'rearport'],
    'consoleserverport': ['consoleport', 'frontport', 'rearport'],
    'powerport': ['poweroutlet', 'powerfeed'],
    'poweroutlet': ['powerport'],
    'interface': ['interface', 'circuittermination', 'frontport', 'rearport'],
    'frontport': ['consoleport', 'consoleserverport', 'interface', 'frontport', 'rearport', 'circuittermination'],
    'rearport': ['consoleport', 'consoleserverport', 'interface', 'frontport', 'rearport', 'circuittermination'],
    'circuittermination': ['interface', 'frontport', 'rearport'],
}

LENGTH_UNIT_METER = 1200
LENGTH_UNIT_CENTIMETER = 1100
LENGTH_UNIT_MILLIMETER = 1000
LENGTH_UNIT_FOOT = 2100
LENGTH_UNIT_INCH = 2000
CABLE_LENGTH_UNIT_CHOICES = (
    (LENGTH_UNIT_METER, 'Meters'),
    (LENGTH_UNIT_CENTIMETER, 'Centimeters'),
    (LENGTH_UNIT_FOOT, 'Feet'),
    (LENGTH_UNIT_INCH, 'Inches'),
)
RACK_DIMENSION_UNIT_CHOICES = (
    (LENGTH_UNIT_MILLIMETER, 'Millimeters'),
    (LENGTH_UNIT_INCH, 'Inches'),
)

# Power feeds
POWERFEED_TYPE_PRIMARY = 1
POWERFEED_TYPE_REDUNDANT = 2
POWERFEED_TYPE_CHOICES = (
    (POWERFEED_TYPE_PRIMARY, 'Primary'),
    (POWERFEED_TYPE_REDUNDANT, 'Redundant'),
)
POWERFEED_SUPPLY_AC = 1
POWERFEED_SUPPLY_DC = 2
POWERFEED_SUPPLY_CHOICES = (
    (POWERFEED_SUPPLY_AC, 'AC'),
    (POWERFEED_SUPPLY_DC, 'DC'),
)
POWERFEED_PHASE_SINGLE = 1
POWERFEED_PHASE_3PHASE = 3
POWERFEED_PHASE_CHOICES = (
    (POWERFEED_PHASE_SINGLE, 'Single phase'),
    (POWERFEED_PHASE_3PHASE, 'Three-phase'),
)
POWERFEED_STATUS_OFFLINE = 0
POWERFEED_STATUS_ACTIVE = 1
POWERFEED_STATUS_PLANNED = 2
POWERFEED_STATUS_FAILED = 4
POWERFEED_STATUS_CHOICES = (
    (POWERFEED_STATUS_ACTIVE, 'Active'),
    (POWERFEED_STATUS_OFFLINE, 'Offline'),
    (POWERFEED_STATUS_PLANNED, 'Planned'),
    (POWERFEED_STATUS_FAILED, 'Failed'),
)
POWERFEED_LEG_A = 1
POWERFEED_LEG_B = 2
POWERFEED_LEG_C = 3
POWERFEED_LEG_CHOICES = (
    (POWERFEED_LEG_A, 'A'),
    (POWERFEED_LEG_B, 'B'),
    (POWERFEED_LEG_C, 'C'),
)
