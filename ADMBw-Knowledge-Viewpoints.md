# ADMBw-Viewpoints (MDG-DiagramProfile)

> Quelle: `NAFv4-ADMBw-MDG-2026.05.xml` — automatisch erzeugt (ohne Zeitstempel)
> 52 Viewpoints

## A1 - Meta-Data Definitions
Architectures, particularly large ones, usually require meta-data tags to aid with searching and discovery.

## A2 - Architecture Products
The A2 Viewpoint specifies the structure of an architecture, and the products that describe the architecture. Each product may correspond to an architecture view. This viewpoint also traces the architectures onto the Enterprise Phases they correspond to (see also C2 – Enterprise Vision) and identifi

## A3 - Architecture Correspondence
ISO/IEC/IEEE42010 introduces the idea of architecture correspondence and correspondence rules. Quoting from ISO/IEC/IEEE 42010; “A correspondence defines a relation between AD (Architecture Description) elements. Correspondences are used to express architecture relations of interest within an archit

## A4 - Methodology Used
The A4 Viewpoint specifies the methodology used for the architecting activities. This methodology is described in NAFv4 Chapter 2. The content of the A4 viewpoint can also be modeled in the A1 viewpoint.

## A5 - Architecture Status
Since NAFv3.0, it has been possible to assign version numbers to views and specify their approval dates. In NAFv4.0, this is integrated with the meta-model’s generic project and milestone approach so that architecture releases are tracked against the architecture delivery project. The content of the

## A6 - Architecture Version
Where the A5 Viewpoint shows the current version number and approval status for the architecture, the A6 Viewpoint shows the complete history of the architecture.

## A7 - Architecture Compliance
The A7 Viewpoint gives the overall specification of architecture meta-data.

## A8 - Standards
The A8 Viewpoint encompasses both technical and non-technical standards. The standards specified in the A8 view can be applied across the architecture to a variety of structural and behavioural elements. Standards are essential to the coherent running of businesses and to the delivery of reliable, i

## Ar - Architecture Roadmap
The Ar Viewpoint shows the history of the architecture project as well as its future direction.

## C1 - Capability Taxonomy
The C1 Viewpoint specifies all the capabilities that are referenced throughout one or more architectures – i.e. one C1 may provide the definitive list of capabilities for a number of logical and resource architectures. The capabilities may be organised into specialisation hierarchies (taxonomies). M

## C2 - Enterprise Vision
The purpose of the C2 Viewpoint is to provide a strategic context for the capabilities described in the architecture and to specify the scope for the architecture. The C2 Viewpoint is high-level and describes the vision, goals, enduring tasks and capabilities using terminology that is easily underst

## C3 - Capability Dependencies
The C3 Viewpoint is intended to provide a means of analysing the dependencies between capabilities and between capability clusters. The composition of capabilities (into clusters) is logical and the purpose of the clusters is to guide enterprise management.

## C4 - Standard Processes
The C4 Viewpoint specifies Standard Operational Activities that can be re-used across multiple logical architectures (e.g. in L4, Logical Activities).

## C5 - Effects
The purpose of the C5 Viewpoint is to describe the operational effect of the capabilities, activities and services according to the expected goals. The C5 Viewpoint is high-level description that should be easily understood by non-technical readers.

## C7 - Performance Parameters
In the C7 Viewpoint the capability requirements (and existing capabilities) can be expressed in terms of Measures of Effectiveness (MoEs). These are high-level metrics used to judge the level of capability.

## C8 - Planning Assumptions
The C8 Viewpoint is concerned with identification and description of assumptions that have been made for the implementation of capabilities. Assumptions can be expressed by means of requirements.

## Cr - Capability Roadmap
The Cr Viewpont supports the Capability Audit process by providing a method to identify gaps or duplications in capability provision. Cr indicates capability increments, which are derived from delivery milestones within acquisition projects.

## L1 - Node Types
The L1 Viewpoint defines all of the Nodes that will appear in a Logical Architecture. Nodes are elements of capability assembled and orchestrated in the Logical Architecture (see L2 - Logical Scenario and L4 - Logical Activities views). The levels of capability provided by each node are expressed as

## L2 - Logical Scenario
The L2 Viewpoint specifies Nodes (elements of capability) in context of each other. The context is usually expressed in terms of the information that flows between the nodes (e.g. the information flow requirements between capabilities in a given scenario) but may also be flows of materiel, human res

## L3 - Node Interactions
L3 is used to provide further detail of the interoperability requirements associated with the operational capability of interest. The focus is on logical flows that cross the capability boundary. Although the primary purpose of the L3 Viewpoint is to specify information exchanges, the L3 may also li

## L4 - Logical Activities
The L4 Viewpoint describes the operational activities that are being conducted within the mission or scenario. These activities are defined at a logical, solution-neutral level so as to enable different solutions in the physical layer. The L4 Viewpoint describes the activities associated with the lo

## L5 - Logical States
The L5 Viewpoint specifies the typical states a node may have and the possible transitions between those states (i.e. changes of state). Triggers for state changes may also be defined. Actions may be associated with a given state or with the transition between states in response to stimuli (e.g. tri

## L6 - Logical Sequence
Operational Event-Trace Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between nodes in a scenario or critical sequence of events. The node interactions usually correspond to flows of information but may describe flows of energ

## L7 - Information Model
The L7 Viewpoint is used to document the business information. It describes the information that can be exchanged along the logical flows in the architecture, specified in L3 Node Interactions.

## L8 - Logical Constraints
The L8 Viewpoint is used to constrain the logical architecture without forcing a particular solution. L8 is used for rules which are not expressed as behavioural models, interactions or measures of effectiveness, i.e. they are textual statements of requirements that constrain the architecture.

## Lr - Lines of Development
The Lr Viewpoint is primarily intended to support the acquisition process across multiple projects or programmes, highlighting dependencies the logical dependencies between capabilities, projects and the integration of all lines of development to achieve a successfully integrated military capability

## L2-L3 - Logical Concept
The L2-L3 Viewpoint is concerned with providing an executive level, scenario-based communication of the architecture purpose, scope and content.

## P1 - Resource Types
The P1 Viewpoint collects together all the Resource Types in the architecture together with a depiction of their performance characteristics. P1 also provides a summary of the technologies and competencies that impact on the Resources that constitute the architecture.

## P2 - Resource Structure
The P2 Viewpoint links together the operational and physical architecture viewpoints by depicting how types of Resource are structured and interact to realize the logical architecture specified in L2, Logical Scenario. The P2 Viewpoint may represent the realization of a requirement specified in a L2

## P3 - Resource Connectivity
The networks and pathways documented in a P3 Viewpoint represent the physical implementation of the logical flows identified in a L2, Logical Scenario, or L3, Node Interactions View.

## P4 - Resource Functions
The Functionality Description provides detailed information regarding the allocation of functions to resources, and flows between Resource Functions. The P4 Viewpoint is the Physical Resource counterpart to the L4 Logical Activities Viewpoint.

## P5 - Resource States
The P5 Viewpoint identifies the states a Resource can be, the allowable changes between those states, and the stimuli (e.g. triggers and events) that cause the state changes.

## P6 - Resource Sequence
The P6 Viewpoint is valuable for moving to the next level of detail from the initial solution design, to help define a sequence of functions and Resource Interactions, and to ensure that each participating Resource or Port has the necessary information, at the right time, in order to perform its ass

## P7 - Data Model
The P7 Viewpoint is one of the architectural products closest to actual system design in the NAF. It is used to describe how the information represented in the L7 Logical Data Model Viewpoint is implemented.

## P8 - Resource Constraints
The P8 Viewpoint describes constraints on the Resources, Resource Functions, data and communications that make up a Physical Architecture.

## Pr - Configuration Management
The Pr Viewpoint provides an overview of how Resource Assets change over time (note that NAF v3.1 only allowed for Capability Configurations whereas now this is opened up to all Resource Types). It shows the structure of different versions of Resource Assets (usually Capability Configurations or Ser

## L4-P4 - Activity To Function Mapping
The L4-P4 Viewpoint depicts the mapping of Resource Functions (and optionally, the resources that provide them) to operational activities and/or service functions. For operational activities it thus identifies the transformation of an operational need into a purposeful action performed by a system o

## R2 - Requirement Catalogue
The R2 represents a catalog of requirements in the architectural model. For this purpose, categories can be created in which the functional and non-functional requirements can be grouped.

## R3 - Requirement Dependencies
The R3 is used to show dependencies between different requirements.

## R7 - Requirement Derivation
The R7 assigns functional and non-functional requirements to the demanding architectural elements. In addition, information about the planned realization can be shown.

## R8 - Requirement Fulfilment
The R8 is used to determine and map acceptance and evaluation criteria for the individual functional and non-functional requirements.

## Rr - Requirement Realization
In the Rr, requirements are assigned to the realizing architectural elements.

## S1 - Service Taxonomy
The purpose of the S1 Viewpoint is to provide a governance structure for a Service-Oriented Architecture. Along with S3, Service Interfaces, it specifies a standard library of service specifications for an enterprise, to which service implementers are expected to conform.

## S2 - Service Structure
The S2 Viewpoint is concerned with identification and description of how services are structured to create a higher-aggregated service. To provide highlevel views, dependencies to other services, nodes and resources as well as service interfaces and service functions can be represented.

## S3 - Service Interfaces
The S3 Viewpoint is concerned with the identification and definition of service interfaces.

## S4 - Service Functions
The S4 Viewpoint is the key behavioural specification for services. Equivalent in nature to L4, Logical Activities and P4, Resources Functions, it specifies a set of functions that a service implementation is expected to perform. Implementation of that behaviour is represented in P4, Resource Functi

## S5 - Service States
The S5 Viewpoint is a specification of the allowable states of a service, and the possible transitions between them. This specification constrains how implementations of the service will behave. It is, though, generally considered a good practice to make services stateless - i.e. consumers of a serv

## S6 - Service Interactions
Service Interaction Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between services in a composition or critical sequence of events.

## S7 - Service Interface Parameters
Specifies the interfaces that a service provides and uses, defines which services are compatible with which other services.

## S8 - Service Policy
The S8 Viewpoint specifies constraints against services to which implementations must conform.

## Sr - Service Roadmap
The Sr Viewpoint supports the Service Audit process by providing a method to identify gaps or duplications in service provision. Sr indicates service lifetime evolutions, which are derived from delivery milestones within acquisition projects.

## C1-S1 - Capability to Service Mapping
A C1-S1 Viewpoint presents a simple mapping of services to capabilities, showing which services contribute to which capability.
