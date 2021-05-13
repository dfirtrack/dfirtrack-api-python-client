# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from dfirtrackapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dfirtrackapi_client.model.analysisstatus import Analysisstatus
from dfirtrackapi_client.model.artifact import Artifact
from dfirtrackapi_client.model.artifactpriority import Artifactpriority
from dfirtrackapi_client.model.artifactstatus import Artifactstatus
from dfirtrackapi_client.model.artifacttype import Artifacttype
from dfirtrackapi_client.model.auth_token import AuthToken
from dfirtrackapi_client.model.case import Case
from dfirtrackapi_client.model.casepriority import Casepriority
from dfirtrackapi_client.model.casestatus import Casestatus
from dfirtrackapi_client.model.casetype import Casetype
from dfirtrackapi_client.model.company import Company
from dfirtrackapi_client.model.contact import Contact
from dfirtrackapi_client.model.division import Division
from dfirtrackapi_client.model.dnsname import Dnsname
from dfirtrackapi_client.model.domain import Domain
from dfirtrackapi_client.model.domainuser import Domainuser
from dfirtrackapi_client.model.ip import Ip
from dfirtrackapi_client.model.location import Location
from dfirtrackapi_client.model.os import Os
from dfirtrackapi_client.model.osarch import Osarch
from dfirtrackapi_client.model.reason import Reason
from dfirtrackapi_client.model.recommendation import Recommendation
from dfirtrackapi_client.model.serviceprovider import Serviceprovider
from dfirtrackapi_client.model.system import System
from dfirtrackapi_client.model.systemstatus import Systemstatus
from dfirtrackapi_client.model.systemtype import Systemtype
from dfirtrackapi_client.model.systemuser import Systemuser
from dfirtrackapi_client.model.tag import Tag
from dfirtrackapi_client.model.tagcolor import Tagcolor
from dfirtrackapi_client.model.task import Task
from dfirtrackapi_client.model.taskname import Taskname
from dfirtrackapi_client.model.taskpriority import Taskpriority
from dfirtrackapi_client.model.taskstatus import Taskstatus
