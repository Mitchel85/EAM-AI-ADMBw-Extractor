# ADMBw-Stereotype (MDG-extrahiert)

> Quelle: `/tmp/NAFv4-ADMBw-MDG-2026.05.xml` — automatisch erzeugt am 2026-10-18 21:50 UTC
> 642 Stereotype · Version: NAFv4-ADMBw-MDG-2026.05.xml

| Stereotype | Metatype | Vererbung | AppliesTo | Beschreibung |
|---|---|---|---|---|
| AchievedEffect | AchievedEffect | MeasurableElement | Dependency | A tuple that exists between an ActualState (e.g., observed/measured during testing) of an element that attempts to achieve a DesiredEffect and an Achiever. |
| Achiever | Achiever | UAFElement | Object | An ActualResource, ActualProject or ActualEnterprisePhase that can deliver a DesiredEffect. |
| ActivityPerformableUnderCondition | ActivityPerformableUnderCondition | MeasurableElement | Dependency | The ActualCondition under which an Activity is performed. |
| ActivitySupportsService | ActivitySupportsService |  | Realisation | Relation states that a process is necessary for the implementation of a service. |
| ActsUpon | ActsUpon |  | Dependency | Asserts that something (subject) is acted upon by an OperationalActivity (activity). |
| ActualCondition | ActualCondition | ActualPropertySet | Object | An individual describing an actual situation with respect to circumstances under which an OperationalActivity, Function or ServiceFunction can be performed. |
| ActualConditionToActualResource | ActualConditionToActualResource |  | Dependency | A relationship that expresses that a actual resource is an actual situation. |
| ActualEnduringTask | ActualEnduringTask | ActualPropertySet | Object | An actual undertaking recognized by an enterprise as being essential to achieving its goals - i.e. a strategic specification of what the enterprise does. |
| ActualEnterprisePhase | ActualEnterprisePhase | Achiever | Object | The ActualState that describes the phase of an Enterprise endeavor. |
| ActualEnvironment | ActualEnvironment | ActualCondition | Object | The ActualState that describes the circumstances of an Environment. |
| ActualLocation | ActualLocation | ActualCondition | Object | The ActualState that describes a physical location, for example using text to provide an address, Geo-coordinates, etc. |
| ActualMeasurement | ActualMeasurement | ActualState | Slot | An actual value that is applied to a Measurement. |
| ActualMeasurementSet | ActualMeasurementSet | ActualPropertySet | Object | A set of ActualMeasurements. |
| ActualMeasurementSetAppliesFor | ActualMeasurementSetAppiesFor |  | Dependency | A relationship that expresses which actual measurement applies for an element. |
| ActualOrganization | ActualOrganization | ActualResponsibleResource | Object | An actual formal or informal organizational unit, e.g. "Driving and Vehicle Licensing Agency", "UAF team Alpha". |
| ActualOrganizationalResource | ActualOrganizationalResource | ActualResource | Object | Abstract element for an ActualOrganization, ActualPerson or ActualPost. |
| ActualOrganizationRole | ActualOrganizationRole | ActualResourceRole | Slot | An ActualOrganizationalResource that is applied to a ResourceRole. |
| ActualPerson | ActualPerson | ActualResponsibleResource | Object | An individual human being. |
| ActualPost | ActualPost | ActualResponsibleResource | Object | An actual, specific post, an instance of a Post "type" - e.g., "President of the United States of America." where the Post would be president. |
| ActualProject | ActualProject | Achiever | Object | A time-limited endeavor to provide a specific set of ActualResource that meet specific Capability needs. |
| ActualProjectConsults | ActualProjectConsults |  | Dependency | A relation that expresses that a project consults an OrganizationalResource. |
| ActualProjectDependency | ActualProjectDependency |  | Dependency | Relationship that is a dependency of a actualproject on a actualproject. |
| ActualProjectInforms | ActualProjectInforms |  | Dependency | A relation that expresses that a project informs an OrganizationalResource. |
| ActualProjectMilestone | ActualProjectMilestone | ActualPropertySet | Object | An event with a start date in a ActualProject from which progress is measured. |
| ActualProjectMilestoneRole | ActualProjectMilestoneRole | ActualState | Slot | An ActualProjectMilestone that is applied to a ProjectMilestoneRole. |
| ActualPropertySet | ActualPropertySet | ActualState | Object | A set or collection of Actual properties. |
| ActualResource | ActualResource | Achiever | Object | Role in an Organisation, where the role carries the authority to undertake a function - through the ActualOrganizationalResource given the role has the responsi |
| ActualResourceNeededByActualProjectMilestone | ActualResourceNeededByActualProjectMilestone |  | Dependency | A relationship that expresses that an actual resource is needed by actual project milestones. |
| ActualResourceRelationship | ActualResourceRelationship | SysML1.4::itemFlow | InformationFlow | An actual resource flow existing between ActualResources (i.e. flow of data, people, materiel, or energy). |
| ActualResourceRole | ActualResourceRole | UAFElement | Slot | An instance of a ResourcePerformer. |
| ActualResourceToActualProjectMilestone | ActualResourceToActualProjectMilestone |  | Dependency | A relationship that expresses that an actual resource is mapped to actual project milestones. |
| ActualResponsibleResource | ActualResponsibleResource | ActualOrganizationalResource | Object | An abstract type grouping responsible OrganizationalResources. |
| ActualService | ActualService | ActualMeasurementSet | Object | An individual ServiceSpecification. |
| ActualServiceSpecificationRole |  |  | Slot | An instance of a ServiceSpecification in context of a ServiceSpecification. |
| ActualState | ActualState | UAFElement | Object | Abstract element that applies temporal extent to a set of elements realized as Instance Specifications. |
| AffectedActivity | AffectedActivity |  | Dependency | A relationship that expresses which resource is affected by a operational activity. |
| AffectedFunctions | AffectedFunctions |  | Dependency | A relationship that expresses which function is affected by a resource. |
| AffectedResource | AffectedResource |  | Dependency | A relationship that expresses which operational activity is affected by a resource. |
| Alias | Alias | MeasurableElement | Note | A metamodel Artifact used to define an alternative name for an element. |
| AlignsWithGoal | AlignsWithGoal |  | Dependency | A relationship that expresses that an element is aligned with a goal. |
| ArbitraryConnector | ArbitraryConnector | MeasurableElement | Dependency | Represents a visual indication of a connection used in high level operational concept diagrams. |
| ArchitecturalDescription | ArchitecturalDescription | MeasurableElement | Package | An Architecture Description is a work product used to express the Architecture of some System Of Interest. It provides executive-level summary information about |
| ArchitecturalReference | ArchitecturalReference | MeasurableElement | Dependency | A tuple that specifies that one architectural description refers to another. |
| ArchitecturalSequence | ArchitecturalSequence | MeasurableElement | Dependency | A relationship that specifies that one architectural description is the successor of another. |
| Architecture | Architecture | UAFElement | Class | An abstract type that represents a generic architecture. Subtypes are OperationalArchitecture and ResourceArchitecture. |
| ArchitectureForProject | ArchitectureForProject |  | Dependency | A relationship that expresses that a architectural description belongs to a actual project. |
| ArchitectureMetadata | ArchitectureMetadata | Metadata | Note | Information associated with an ArchitecturalDescription, that supplements the standard set of tags used to summarize the Architecture. It states things like wha |
| Asset | Asset | ConceptItem | Class | Asset as applied to Security views, an abstract type that indicates the types of elements that can be considered as a subject for security analysis. |
| AssetRole | AssetRole | BPMN2.0::ResourceRole | Part | AssetRole as applied to Security views, an abstract element that indicates the type of elements that can be considered as a subject for security analysis in the |
| BoundaryCondition | BoundaryCondition |  | Dependency | A relationship that expresses which environment is relevant to an resource exchange. |
| BusinessProcess | BusinessProcess | Achiever | Activity | An abstract type that represents a behavior or process (i.e. a Function or OperationalActivity) that can be performed by a Performer. |
| BWRequirement |  |  | Requirement | Abstract base class for requirements. |
| Capability | Capability | Desirer | Class | A high level specification of the enterprise's ability to execute a specified course of action. |
| CapabilityConfiguration | CapabilityConfiguration | ResourceArchitecture | Class | A composite structure representing the physical and human resources (and their interactions) in an enterprise, assembled to meet a capability). |
| CapabilityDependency | CapabilityDependency | MeasurableElement | Dependency | A tuple that asserts that one Capability is dependent from another. |
| CapabilityForTask | CapabilityForTask | MeasurableElement | Abstraction | A tuple that asserts that a Capability is required in order for an Enterprise to conduct a phase of an EnduringTask. |
| CapabilityGeneralization | CapabilityGeneralization | PropertySetGeneralization | Generalization | A CapabilityGeneralization is a taxonomic relationship between a more general Capability and a more specific Capability. |
| CapabilityRole | CapabilityRole | Desirer | Part | A high level specification of the enterprise's ability to execute a specified course of action. |
| CapabilityRoleDependency | CapabilityRoleDependency | MeasurableElement | Dependency | A tuple that asserts that one CapabilityRole is dependent from another. |
| CapableElement | CapableElement | UAFElement |  | An abstract type that represents a structural element that can perform behaviors (i.e. OperationalActivity). |
| Checks | Checks |  | Dependency | Relation that shows that an acceptance criterion (FitCriterion) is valid for a functional or non-functional requirement. |
| Classification | Classification |  | Class | Classification according to STANAG 1059. |
| Classified | Classified |  | Dependency | Relationship that indicates which classification an element has. |
| Command | Command | ResourceExchange | InformationFlow | A type of ResourceExchange that asserts that one OrganizationalResource commands another. |
| Competence | Competence | PropertySet | Class | A specific set of abilities defined by knowledge, skills and aptitude. |
| CompetenceForRole | CompetenceForRole |  | Dependency | A tuple used to associate an organizational role with a specific set of required competencies. |
| CompliesViewpoint | CompliesViewpoint |  | Dependency | Relationship that expresses that a view has been created according to the specifications of a viewpoint. |
| ConceptItem | ConceptItem | UAFElement |  | Abstract, an item which may feature in a HighLevelOperationalConcept. |
| ConceptRole | ConceptRole | MeasurableElement | Part | Usage of a ConceptItem in the context of a HighLevelOperationalConcept. |
| Concern | Concern | PropertySet | Class | Interest in an EnterprisePhase (EnterprisePhase is synonym for System in ISO 42010) relevant to one or more of its stakeholders. |
| ConcernForActualEnterprisePhase | ConcernForActualEnterprisePhase |  | Dependency | A relationship that expresses which concerns are covered by an actual enterprise phase. |
| ConcernForView | ConcernForView |  | Dependency | A relationship that expresses which concerns are covered by view. |
| ConcernForViewpoint | ConcernForViewpoint |  | Dependency | A relationship that expresses which concerns are covered by viewpoint. |
| Condition | Condition | PropertySet | Class, DataType | A type that defines the Location, Environment and/or GeoPoliticalExtent. |
| ConflictsWith | ConflictsWith |  | Dependency | Relation that represents a conflict between two requirements. |
| ConformsTo | ConformsTo |  | Dependency | A relationship that expresses that an UAFElement conforms to a standard. |
| ConsumedBy | ConsumedBy |  | Dependency | Asserts that a service is consumed by a node. It is not required to know what provides the service. |
| Consumes | Consumes | MeasurableElement | Abstraction | A tuple that asserts that a service in someway contributes or assists in the execution of an OperationalActivity. |
| Control | Control | ResourceExchange | InformationFlow | A type of ResourceExchange that asserts that one PhysicalResource controls another PhysicalResource (i.e. the driver of a vehicle controlling the vehicle speed  |
| DataElement | DataElement | ResourceAsset | Class | A formalized representation of data that is managed by or exchanged between resources. |
| DataElementStoredIn | DataElementStoredIn | StoredIn | Dependency | Relation says that a data is stored in software. |
| DataModel | DataModel | SubjectOfOperationalConstraint | Package | A structural specification of data types, showing relationships between them that is devoid of implementation detail. The type of data captured in the DataModel |
| DataRole | DataRole | AssetRole | Part | A usage of DataElement that exists in the context of an ResourceAsset. It also allows the representation of the whole-part aggregation of DataElements. |
| Definition | Definition | MeasurableElement | Note | A comment containing a description of an element in the architecture. |
| DerivedFrom | DerivedFrom |  | Dependency | Relation that shows that a functional or non-functional requirement is based on a process, role and task carrier, information element or other element. |
| DescribedBy | DescribedBy |  | Dependency | A relationship that expresses that an architectural description describes an architecture. |
| DesiredEffect | DesiredEffect | MeasurableElement | Dependency | A tuple relating the Desirer (a Capability or OrganizationalResource) to an ActualState. |
| Desirer | Desirer | UAFElement |  | Abstract type used to group architecture elements that might desire a particular effect. |
| DocumentReference | DocumentReference | Reference | Class | The element describes a regulation, instruction or a general document. |
| ElementCatalogue |  |  | Package |  |
| EnduringTask | EnduringTask | PropertySet | Class | A type of template behavior recognized by an enterprise as being essential to achieving its goals - i.e. a template for a strategic specification of what the en |
| Energy | Energy | PhysicalResource | Class | A representation of any kind of energy. |
| EnterpriseGoal | EnterpriseGoal | PropertySet | Class | A statement about a state or condition of the enterprise to be brought about or sustained through appropriate Means. An EnterpriseGoal amplifies an EnterpriseVi |
| EnterprisePhase | EnterprisePhase | PropertySet | Class | A current or future state of the wholeLifeEnterprise or another EnterprisePhase. |
| EnterpriseVision | EnterpriseVision | PropertySet | Class | A Vision describes the future state of the enterprise, without regard to how it is to be achieved. |
| Environment | Environment | Condition | Class | A definition of the environmental factors in which something exists or functions. The definition of an Environment element can be further defined using Environm |
| EnvironmentalCondition | EnvironmentalCondition |  | Dependency | Relationship that indicates under which environment an exhibits-relationship takes place. |
| EnvironmentalContext | EnvironmentalContext |  | Dependency | Relationship that indicates under which condition an measurement counts. |
| EnvironmentProperty | EnvironmentProperty | MeasurableElement | Class | A property of an Environment that is typed by a Condition. The kinds of Condition that can be represented are Location, GeoPoliticalExtentType and Environment. |
| Evaluates | Evaluates |  | Realisation | This relation states that an evaluation criterion (FulfilmentCriterion) can be assigned to a specific acceptance criterion (FitCriterion). |
| Exchange | Exchange | BPMN2.0::MessageFlow |  | Abstract tuple, grouping OperationalExchanges and ResourceExchanges that exchange Resources. |
| ExchangeItem | ExchangeItem |  |  | An abstract grouping for elements that defines the types of elements that can be exchanged between Assets and conveyed by an Exchange. |
| Exhibits | Exhibits | MeasurableElement | Abstraction | A tuple that exists between a CapableElement and a Capability that it meets under specific environmental conditions. |
| Expresses | Expresses |  | Dependency | A relationship that expresses that an architectural description includes the following architectures. |
| FieldedCapability | FieldedCapability | ActualResource | Object | An individual, fully-realized capability. |
| FillsPost | FillsPost | MeasurableElement | Dependency | A tuple that asserts that an ActualPerson fills an ActualPost. |
| Finding | Finding |  | Class | An ascertainment made in the model, which relates to the methodology used, the subject under consideration, the tool or something else. |
| FitCriterion | FitCriterion |  | Class | This element represents an acceptance criterion for a functional or non-functional requirement. |
| Forecast | Forecast | MeasurableElement | Dependency | A tuple that specifies a transition from one Asset, Standard, Competence to another future one. It is related to an ActualEnterprisePhase to give it a temporal  |
| ForecastPeriod | ForecastPeriod |  | Dependency | Planning phase for which the forecast is valid. |
| FormStoredIn | FormStoredIn | StoredIn | Dependency | Relation states that a digital form is stored in software. |
| FulfilmentCriterion | FulfilmentCriterion |  | Class | This element represents a criterion for evaluating the degree of implementation of a functional or non-functional requirement. |
| Function | Function | BusinessProcess | Activity | An Activity which is specified in the context to the ResourcePerformer (human or machine) that IsCapableToPerform it. |
| FunctionAction | FunctionAction | ProcessUsage | Action | A call of a Function indicating that the Function is performed by a ResourceRole in a specific context. |
| FunctionalRequirement | FunctionalRequirement | BWRequirement | Requirement | The element represents a functional requirement (what should the system / software be able to do?). |
| FunctionControlFlow | FunctionControlFlow | FunctionEdge | ControlFlow | An ActivityEdge that shows the flow of control between FunctionActions. |
| FunctionEdge | FunctionEdge | ProcessEdge |  | A tuple that shows the flow of Resources (objects/data) between FunctionActions. |
| FunctionObjectFlow | FunctionObjectFlow | FunctionEdge | ObjectFlow | An ActivityEdge that shows the flow of Resources (objects/data) between FunctionActions. |
| FunctionSubject | FunctionSubject |  | Dependency | A relationship that expresses that a function uses certain resources. |
| GeoPoliticalExtentType | GeoPoliticalExtentType | Condition | DataType | A geospatial extent whose boundaries are defined by declaration or agreement by political parties. |
| GoalForActualEnterprisePhase | GoalForActualEnterprisePhase |  | Dependency | A relationship that expresses which actual enterprisephase implements an enterprisegoal. |
| HighLevelOperationalConcept | HighLevelOperationalConcept | PropertySet | Class | Describes the Resources and Locations required to meet an operational scenario from an integrated systems point of view. It is used to communicate overall quant |
| HostedOn | HostedOn |  | Dependency | Relation states that hardware (virtualized) or software is hosted on a virtualized platform or physical hardware. |
| Implements | Implements | MeasurableElement | Abstraction | A tuple that defines how an element in the upper layer of abstraction is implemented by a semantically equivalent element (i.e. tracing the OperationalActivitie |
| ImplementsProtocol | ImplementsProtocol |  | Dependency | A relationship that expresses which protocol implements an architectural element. |
| Information | Information | MeasurableElement | Note | A comment that describes the state of an item of interest in any medium or form -- and is communicated or received. |
| InformationElement | InformationElement | OperationalAsset | Class | An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are cap |
| InformationRole | InformationRole | AssetRole | Part | A usage of InformationElement that exists in the context of an OperationalAsset. It also allows the representation of the whole-part aggregation of InformationE |
| InteractionMessage | InteractionMessage | MeasurableElement | Message | An abstract type that groups several types of messages used in the InteractionScenario. |
| InteractionRole | InteractionRole |  | Lifeline | An abstract type that represents an individual participant in the InteractionScenario. |
| IsAccountableFor | IsAccountableFor |  | Dependency | A relation that expresses that an OrganizationalResource is responsible for a resource, service or project in the context of an approval. |
| IsCapableToPerform | IsCapableToPerform | MeasurableElement | Abstraction | A relationship that says that a capable element performs an activity or action. |
| IsDuplicateOf | IsDuplicateOf |  | Dependency | Relation that represents that two requirements convey the same content. |
| IsEquivalentToStandardElement | IsEquivalentToStandardElement |  | Dependency | Relationship that indicates that a model element corresponds to a catalog element. |
| IsResponsibleFor | IsResponsibleFor |  | Dependency | A relation that expresses that an OrganizationalResource is responsible for a resource, service or project. |
| JustifiedBy | JustifiedBy |  | Dependency | Relation states that an Constraint is derived from a reference (Reference, DocumentReference, SMEReference). |
| KnownResource | KnownResource | OperationalPerformer | Class | Asserts that a known ResourcePerformer constrains the implementation of the OperationalPerformer that plays the role in the LogicalArchitecture. |
| Location | Location | ConceptItem | Class, DataType | A specification of the generic area in which a LocationHolder is required to be located. |
| LocationHolder | LocationHolder | UAFElement |  | Abstract type, used to group elements that are allowed to be associated with a Location. |
| LocationType | LocationType |  | Dependency | A relationship that expresses which location is assigned to a location holder. |
| MapsToCapability | MapsToCapability | MeasurableElement | Abstraction | A tuple denoting that an Activity contributes to providing a Capability. |
| MeasurableElement | MeasurableElement | UAFElement |  | Abstract type, grouping elements that can be measured by applying MeasurementSets to them. |
| Measurement | Measurement | MeasurableElement | Part | A property of an element representing something in the physical world, expressed in amounts of a unit of measure. |
| MeasurementType | MeasurementType |  | Class | A type of a property representing something in the physical world, expressed in amounts of a unit of measure. |
| Metadata | Metadata | MeasurableElement | Note | A comment that can be applied to any element in the architecture. The attributes associated with this element details the relationship between the element and i |
| MilestoneDependency | MilestoneDependency | MeasurableElement | Dependency | A tuple between two ActualProjectMilestones that denotes one ActualProjectMilestone follows from another. |
| NaturalResource | NaturalResource | PhysicalResource | Class | Type of physical resource that occurs in nature. |
| NeedsModificationOf | NeedsModificationOf |  | Dependency | Relation stats that a project makes adjustments to a resource. |
| NeedsResource | NeedsResource |  | Dependency | Relation stats that a project needs a resource. |
| NeedsService | NeedsService |  | Dependency | A relation that expresses that a project needs a service |
| NonfunctionalRequirement | NonfunctionalRequirement | BWRequirement | Requirement | The element represents a non-functional requirement (how should the system / software be able to do something?). |
| OperationalActivity | OperationalActivity | BusinessProcess | Activity | An Activity that captures a logical process, specified independently of how the process is carried out. |
| OperationalActivityAction | OperationalActivityAction | MeasurableElement | Action | A call of an OperationalActivity in the context of another OperationalActivity. |
| OperationalActivityEdge | OperationalActivityEdge | ProcessEdge |  | A tuple that shows the flow of Resources (objects/information) between OperationalActivityActions. |
| OperationalAgent | OperationalAgent | CapableElement | Class | An abstract type grouping Operational Architecture and Operational Performer. |
| OperationalArchitecture | OperationalArchitecture | Architecture | Class | A type used to denote a model of the Architecture, described from the Operational perspective. |
| OperationalArchitectureOfEnterprisePhase | OperationalArchitectureOfEnterprisePhase |  | Dependency | Relationship that says that in a actual enterprisephase an operational architecture is valid. |
| OperationalAsset | OperationalAsset | Asset | Class | An abstract element used to group the elements of OperationalAgent and InformationElement allowing them to own InformationRoles. |
| OperationalConnector | OperationalConnector | MeasurableElement | Connector | A Connector that goes between OperationalRoles representing a need to exchange Resources. It can carry a number of OperationalExchanges. |
| OperationalConstraint | OperationalConstraint | Rule | Class | A Rule governing a logical architectural element i.e. OperationalPerformer, OperationalActivity, InformationElement etc. |
| OperationalControlFlow | OperationalControlFlow | OperationalActivityEdge | ControlFlow | An ActivityEdge that shows the flow of control between OperationalActivityActions. |
| OperationalExchange | OperationalExchange | Exchange | InformationFlow | Asserts that a flow can exist between OperationalPerformers (i.e. flows of information, people, materiel, or energy). |
| OperationalExchangeItem | OperationalExchangeItem | ExchangeItem |  | An abstract grouping for elements that defines the types of elements that can be exchanged between OperationalPerformers and conveyed by an OperationalExchange. |
| OperationalInterface | OperationalInterface | PropertySet | Class | A declaration that specifies a contract between the OperationalPerformer it is related to, and any other OperationalPerformers it can interact with. |
| OperationalMessage | OperationalMessage | InteractionMessage | Message | Message for use in an Operational Event-Trace which carries any of the subtypes of OperationalExchange. |
| OperationalMessageFlow | OperationalMessageFlow | BPMN2.0::MessageFlow | ControlFlow | A ProcessMessageFlow that shows the flow of message between OperationalActivityActions of different ActivityPartitions like Pools. |
| OperationalMethod | OperationalMethod | ProcessOperation | Operation | behavioral feature of a OperationalPerformer whose behavior is specified in an OperationalActivity. |
| OperationalObjectFlow | OperationalObjectFlow | OperationalActivityEdge | ObjectFlow | An ActivityEdge that shows the flow of Resources (objects/information) between OperationalActivityActions. |
| OperationalParameter | OperationalParameter | ProcessParameter | Parameter | A type that represents inputs and outputs of an OperationalActivity. It is typed by an OperationalExchangeItem. |
| OperationalPerformer | OperationalPerformer | OperationalAgent | Class | A logical entity that IsCapableToPerform OperationalActivities which produce, consume and process Resources. |
| OperationalPort | OperationalPort | MeasurableElement | Port | An interaction point for an OperationalAgent through which it can interact with the outside environment and which is defined by an OperationalInterface. |
| OperationalRole | OperationalRole | AssetRole | Part | Usage of a OperationalPerformer or OperationalArchitecture in the context of another OperationalPerformer or OperationalArchitecture. Creates a whole-part relat |
| OperationalSignal | OperationalSignal | OperationalExchangeItem | Signal | An item of information that flows between OperationalPerformers and is produced and consumed by the OperationalActivities that the OperationalPerformers are cap |
| OperationalSignalProperty | OperationalSignalProperty | MeasurableElement | Part | A property of an OperationalSignal typed by OperationalExchangeItem. It enables OperationalExchangeItem e.g. InformationElement to be passed as arguments of the |
| OperationalStateDescription | OperationalStateDescription | MeasurableElement | Class | A state machine describing the behavior of a OperationalPerformer, depicting how the OperationalPerformer responds to various events and the actions. |
| Organization | Organization | OrganizationalResource | Class | A group of OrganizationalResources (Persons, Posts, Organizations and Responsibilities) associated for a particular purpose. |
| OrganizationalResource | OrganizationalResource | PhysicalResource | Class | An abstract type for Organization, Person Post and Responsibility. |
| OriginatesFrom | OriginatesFrom |  | Dependency | Relation that derives an element in the architectural model from a reference (Reference, DocumentReference, SMEReference). |
| OwnedMilestone | OwnedMilestone |  | Dependency | Relationship that expresses that actual project has a actual milestone. |
| OwnsActualMeasurementSet | OwnsActualMeasurementSet |  | Dependency | A relationship that expresses which actual measurement set an element owns. |
| OwnsMeasurement | OwnsMeasurement |  | Dependency | A relationship that expresses which measurement or measurement type an element owns. |
| OwnsProcess | OwnsProcess | MeasurableElement | Abstraction | A dependency relationship denoting that an ActualOrganizationResource owns an OperationalActivity. |
| PaperForm | PaperForm |  | Class | Form is a digitized or digitizable document, for example a scanned document. |
| PartOfCatalogue | PartOfCatalogue |  | Aggregation | This relation states that a category (RequirementCategory) belongs to a requirements catalog (RequirementCatalogue). |
| PartOfCategory | PartOfCategory |  | Aggregation | This relation states that his functional or non-functional requirement belongs to a category (RequirementCategory) of the requirements catalog. |
| PerformsInContext | PerformsInContext | MeasurableElement | Abstraction | A relationship that says that a role performs an activity or action. It indicates that the action can be carried out by the role when used in a specific context |
| Person | Person | OrganizationalResource | Class | A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, natio |
| PhysicalArchitectureOfEnterprisePhase | PhysicalArchitectureOfEnterprisePhase |  | Dependency | A relationship that expresses that an actual enterprise phase has resource architectures. |
| PhysicalLocation | PhysicalLocation |  | Dependency | A relationship that expresses that a location holder operates in an actual location. |
| PhysicalResource | PhysicalResource | ResourcePerformer | Class | An abstract type defining physical resources (i.e. OrganizationalResource, ResourceArtifact and NaturalResource). |
| Post | Post | OrganizationalResource | Class | A type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer). |
| PostRole | PostRole | ResourceRole | Part | A usage of a post in the context of another OrganizationalResource. Creates a whole-part relationship. |
| ProblemDomain | ProblemDomain | OperationalRole | Part | A property associated with a logical architecture, used to specify the scope of the problem. |
| ProcessEdge | ProcessEdge | BPMN2.0::SequenceFlow |  | An abstract type that represents a behavior or process (i.e. a Function or OperationalActivity) that can be performed by a Performer. |
| ProcessGeneralization | ProcessGeneralization | MeasurableElement | Generalization | A ProcessGeneralization is a taxonomic relationship between a more general Process and a more specific Process. |
| ProcessMessageFlow | ProcessMessageFlow | BPMN2.0::MessageFlow |  | A tuple that shows the flow of message between different ActivityPartitions like Pools. |
| ProcessOperation | ProcessOperation | MeasurableElement |  | An abstract type that represents a behavior or process (i.e. a Function or OperationalActivity) that can be performed by a Performer. |
| ProcessParameter | ProcessParameter | MeasurableElement |  | An abstract type that represents a behavior or process (i.e. a Function or OperationalActivity) that can be performed by a Performer. |
| ProcessUsage | ProcessUsage | BPMN2.0::Activity |  | An abstract type that represents a behavior or process (i.e. a Function or OperationalActivity) that can be performed by a Performer or Role. |
| Project | Project | OrganizationalResource | Class | A type that describes types of time-limited endeavours that are required to meet one or more Capability needs. |
| ProjectMilestone | ProjectMilestone | PropertySet | Class | A type of event in a Project by which progress is measured. |
| ProjectMilestoneRole | ProjectMilestoneRole | MeasurableElement | Part | The role played by a ProjectMilestone in the context of a Project. |
| ProjectMilestoneToProjectTheme | ProjectMilestoneToProjectTheme |  | Dependency | A relationship that expresses which project theme is handled by which project milestone. |
| ProjectProvidesFunction | ProjectProvidesFunction |  | Dependency | Relation stats that a project realizes a function. |
| ProjectRole | ProjectRole | ResourceRole | Part | Usage of a Project in the context of another Project. Creates a whole-part relationship. |
| ProjectSequence | ProjectSequence | MeasurableElement | Dependency | A tuple between two ActualProjects that denotes one ActualProject cannot start before the previous ActualProject is finished. |
| ProjectStatus | ProjectStatus | ActualState | Slot | The status (i.e. level of progress) of a ProjectTheme for an ActualProject at the time of the ActualProjectMilestone. |
| ProjectSupportActivity | ProjectSupportActivity |  | Dependency | Relation stats that a project supports an activity. |
| ProjectTheme | ProjectTheme | MeasurableElement | Part | A property of a ProjectMilestone that captures an aspect by which the progress of ActualProjects may be measured. |
| PropertySet | PropertySet | MeasurableElement |  | An abstract type grouping architectural elements that can own Measurements. |
| PropertySetGeneralization | PropertySetGeneralisation | MeasurableElement | Generalization | A PropertySetGeneralization is a taxonomic relationship between a more general PropertySet and a more specific PropertySet. |
| Protocol | Protocol | Standard | Class | A Standard for communication over a network. Protocols may be composite, represented as a ProtocolStack made up of ProtocolLayers. |
| ProtocolImplementation | ProtocolImplementation | UAFElement |  | An abstract type grouping architectural elements that can implement Protocols. |
| ProtocolLayer | ProtocolLayer | MeasurableElement | Part | Usage of a Protocol in the context of another Protocol. Creates a whole-part relationship. |
| Protocolstack | Protocolstack | Protocol | Class | A sub type of Protocol that contains the ProtocolLayers, defining a complete stack. |
| ProvidedServiceLevel | ProviededServiceLevel | ActualService | Object | A sub type of ActualService that details a specific service level delivered by the provider. |
| Provides | Provides |  | Dependency | Asserts that a operational agent provides a service. |
| ProvidesCompetence | ProvidesCompetence | MeasurableElement | Dependency | A tuple that asserts that an ActualOrganizationalResource provides a specific set of Competencies. |
| ProvidesServiceFunction | ProvidesServiceFunction |  | Dependency | Relationship that expresses that a service function is provided by an interface. |
| RatifiedStandards | RatifiedStandards |  | Dependency | A relationship that expresses that an actual organization releases a standard. |
| RealiseRequirement | RealiseRequirement |  | Realisation | Relation states that a functional or non-functional requirement is realized through this element. |
| RealizedDesiredEffect | RealizedDesiredEffect |  | Dependency | Relationship that expresses which connector DesiredEffect the connector AchievedEffect realizes. |
| RealizesRecommendation | RealizesRecommendation |  | Realisation | Relation states that a Recommendation is realized through this element. |
| RealizingAchievedEffect | RealizingAchievedEffect |  | Dependency | Relationship that expresses which connector AchievedEffect realizes the connector DesiredEffect. |
| Recommendation | Recommendation |  | Class | Need for action from a finding. |
| Reference | Reference |  | Class | Element describes all types of references. |
| RefersTo | RefersTo |  | Dependency | Relationship that assigns a finding to a recommendation. |
| Refines | Refines |  | Dependency | Relation that represents a refinement of a requirement by another requirement. |
| Replaces | Replaces |  | Dependency | Relation that represents a replacement of a requirement with another requirement. |
| ReplaceStandardElement | ReplaceStandardElement |  | Dependency | Relation that represents a replacement of a standard element with another standard element |
| RequiredEnvironment | RequiredEnvironment |  | Dependency | A relationship that expresses that a location holder operates under specific environmental conditions. |
| RequiredResource | RequiredResource |  | Dependency | Relationship that indicates which resources a project milestone requires |
| RequiredServiceLevel | RequiredServiceLevel | ActualService | Object | A sub type of ActualService that details a specific service level required of the provider. |
| RequirementCatalogue | RequirementCatalogue |  | Class | Element represents a catalog of requirements, which consists of different categories (RequirementCategory) of functional and non-functional requirements. |
| RequirementCategory | RequirementCategory |  | Class | Element represents a category of a catalog of requirements. |
| Requires | Requires |  | Dependency | Relation that represents that a requirement assumes another requirement. |
| RequiresCompetence | RequiresCompetence | MeasurableElement | Abstraction | A tuple that asserts that an ActualOrganizationalResource is required to have a specific set of Competencies. |
| Resource | Resource | PropertySet |  | Abstract element grouping for all elements that can be conveyed by an Exchange. |
| ResourceArchitecture | ResourceArchitecture | Architecture | Class | A type used to denote a model of the Architecture, described from the ResourcePerformer perspective. |
| ResourceArtifact | ResourceArtifact | PhysicalResource | Class | A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.). |
| ResourceAsset | ResourceAsset | Asset | Class | An abstract element used to group the elements of ResourcePerformer and DataElement allowing them to own DataRoles |
| ResourceConnector | ResourceConnector | MeasurableElement | Connector | A channel for exchange between two ResourceRoles. |
| ResourceConstraint | ResourceConstraint | Rule | Class | A rule governing the structural or functional aspects of an implementation. |
| ResourceDependency | ResourceDependency |  | Dependency | Relationship that is a dependency of a resource on a resource. |
| ResourceExchange | ResourceExchange | Exchange | InformationFlow | Asserts that a flow can exist between ResourcePerformers (i.e. flows of data, people, material, or energy). |
| ResourceExchangeItem | ResourceExchangeItem | ExchangeItem |  | An abstract type grouping elements that defines the types of elements that can be exchanged between ResourcePerformers and conveyed by a ResourceExchange. |
| ResourceInterface | ResourceInterface | PropertySet | Class | A declaration that specifies a contract between the ResourcePerformers it is related to and any other ResourcePerformers it can interact with. It is also intend |
| ResourceMessage | ResourceMessage | InteractionMessage | Message | Message for use in an Resource Event-Trace which carries any of the subtypes of ResourceExchange. |
| ResourceMethod | ResourceMethod | ProcessOperation | Operation | A behavioral feature of a ResourcePerformer whose behavior is specified in a Function. |
| ResourceMitigation | ResourceMitigation | ResourceArchitecture | Class | A set of measures intended to implement an OperationalMitigation. Comprises a subset of activities that are performed in mitigation of the risk to protect the a |
| ResourceParameter | ResourceParameter | ProcessParameter | Parameter | A type that represents inputs and outputs of an Function. It is typed by a ResourceInteractionItem. |
| ResourcePerformer | ResourcePerformer | CapableElement | Class | An abstract grouping of elements that can perform Functions. |
| ResourcePort | ResourcePort | MeasurableElement | Port | An interaction point for a ResourcePerformer through which it can interact with the outside environment and which is defined by a ResourceInterface. |
| ResourceRole | ResourceRole | AssetRole | Part | Usage of a ResourcePerformer in the context of another ResourcePerformer. Creates a whole-part relationship. |
| ResourceSignal | ResourceSignal | ResourceExchangeItem | Signal | A property of an element representing something in the physical world, expressed in amounts of a unit of measure. |
| ResourceSignalProperty | ResourceSignalProperty | MeasurableElement | Part | A property of an ResourceSignal typed by ResourceExchangeItem. It enables ResourceExchangeItem e.g. DataElement to be passed as arguments of the ResourceSignal. |
| ResourceStateDescription | ResourceStateDescription | MeasurableElement | StateMachine | A state machine describing the behavior of a ResourcePerformer, depicting how the ResourcePerformer responds to various events and the actions. |
| ResourceToServiceDependency | ResourceToServiceDependency |  | Dependency | Relation states that a resource is dependent on a service. |
| Responsibility | Responsibility | OrganizationalResource | Class | The type of duty required of a Person or Organization. |
| Responsible | Responsible |  | Dependency | Relation states that a project is responsible for a service or a material resource. |
| ResultsFrom | ResultsFrom |  | Dependency | Relationship expresses that an element of architecture is the reason for a finding. |
| Rule | Rule | MeasurableElement | Constraint | An abstract type for all types of constraint (i.e. an OperationalConstraint could detail the rules of accountancy best practice). |
| SameAs | SameAs | MeasurableElement | Dependency | A tuple that asserts that two elements refer to the same real-world thing. |
| Satisfy | Satisfy |  | Dependency | This relation states that an constraint affects an element. |
| SecurityConstraint | SecurityConstraint | Rule | Constraint | A type of rule that captures a formal statement to define security laws, regulations, guidances, and policy. Element is not used in the current version of the f |
| SecurityEnclave | SecurityEnclave | ResourceArchitecture | Class | Collection of information systems connected by one or more internal networks under the control of a single authority and security policy. The systems may be str |
| SecurityProcess | SecurityProcess | Function | Activity | The security-related procedure that satisfies the security control requirement. Element is not used in the current version of the framework and reserved for fut |
| ServiceConnector | ServiceConnector | MeasurableElement | Connector | A channel for exchange between two ServiceSpecifications. Where one acts as the consumer of the other. |
| ServiceDependency | ServiceDependency |  | Dependency | Relationship that is a dependency of a service on a service, operational node or resource. |
| ServiceExchange |  | Exchange | InformationFlow | Asserts that a flow can exist between Services (i.e., flows of information, people, material, or energy). |
| ServiceFunction | ServiceFunction | BusinessProcess | Activity | An Activity that describes the abstract behavior of ServiceSpecifications, regardless of the actual implementation. |
| ServiceFunctionAction | ServiceFunctionAction | ProcessUsage | Action | A call of a ServiceFunction in the context of another ServiceFunction. |
| ServiceGeneralization | ServiceGeneralization | PropertySetGeneralization | Generalization | A ServiceGeneralization is a taxonomic relationship between a more general ServiceSpecification and a more specific ServiceSpecification. |
| ServiceInterface | ServiceInterface | PropertySet | Class | A contract that defines the ServiceMethods and ServiceMessageHandlers that the ServiceSpecification realizes. |
| ServiceMessage | ServiceMessage | InteractionMessage | Message | Message for use in a Service Event-Trace. |
| ServiceMethod | ServiceMethod | MeasurableElement | Operation | A behavioral feature of a ServiceSpecification whose behavior is specified in a ServiceFunction. |
| ServiceParameter | ServiceParameter | ProcessParameter | Parameter | A type that represents inputs and outputs of a ServiceFunction, represents inputs and outputs of a ServiceSpecification. |
| ServicePolicy | ServicePolicy | Rule | Class | A constraint governing the use of one or more ServiceSpecifications. |
| ServicePort | ServicePort | MeasurableElement | Port | An interaction point for a ServiceSpecification through which it can interact with the outside environment and which is defined by a ServiceInterface. |
| ServiceProvision | ServiceProvision | MeasurableElement | Abstraction | An assertion that a Resource delivers a Service to a specified ServiceLevel. |
| ServiceSpecification | ServiceSpecification | Achiever | Class | The specification of a set of functionality provided one element for the use of others. |
| ServiceSpecificationRole | ServiceSpecificationRole | InteractionRole | Part | An assertion that a ServiceSecification calls upon another ServiceSpecification in order to deliver its stated functionality. |
| ServiceStateDescription | ServiceStateDescription | MeasurableElement | StateMachine | A state machine descripting the behavior of a ServiceSpecification, depicting how the ServiceSpecification responds to various events and the actions. |
| SMEReference | SMEReference | Reference | Class | Element stands for a result of a workshop or expert knowledge. |
| Software | Software | ResourceArtifact | Class | A sub-type of ResourceArtifact that specifies an executable computer program. |
| Stakeholder | Stakeholder | UAFElement |  | individual, team, organization, or classes thereof, having an interest in an EnterprisePhase [ISO/IEC/IEEE 42010:2011]. |
| StakeholderConcern | StakeholderConcern |  | Dependency | A relationship that expresses which concern a stakeholder has. |
| Standard | Standard | PropertySet | Class | A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture. |
| StandardOperationalActivity | StandardOperationalActivity | Achiever | Activity | A sub-type of OperationalActivity that is a standard operating procedure. |
| StateDescription | StateDescription |  | StateMachine | An abstract type that represents a state machine (i.e. an OperationalStateDescription or ResourceStateDescription), depicting how the Asset responds to various  |
| StatementTask | StatementTask |  | Dependency | A relationship that expresses that an actual enterprise phase fulfills a actual enduring task. |
| StemsFrom | StemsFrom |  | Dependency | Relationship that states that one requirement stems from another. |
| StoredIn | StoredIn |  | Dependency | Relation states that a digital form or data is stored in software. |
| StrategicConstraint | StrategicConstraint | Rule | Class | A Rule governing a capability. |
| SubjectOfForecast | SubjectOfForecast | UAFElement | Class | An abstract type grouping elements that can be the subject of a Forecast. |
| SubjectOfOperationalConstraint | SubjectOfOperationalConstraint | UAFElement |  | An abstract type grouping elements that can be the subject of an OperationalConstraint. |
| SubjectOfResourceConstraint | SubjectOfResourceConstraint | UAFElement |  | An abstract type grouping elements that can be the subject of a ResourceConstraint. |
| SubjectOfSecurityConstraint | SubjectOfSecurityConstraint | UAFElement |  | An abstract grouping of elements that can be the subject of a SecurityConstraint. Element is not used in the current version of the framework and reserved for f |
| SubOrganization | SubOrganization | ResourceRole | Part | A type of a human being used to define the characteristics that need to be described for ActualPersons (e.g. properties such as address, telephone number, natio |
| SuccessorOf |  |  | Dependency | A relationship between two elements that indicates that one element is the successor of the other. |
| System | System | ResourceArchitecture | Class | An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), pr |
| Technology | Technology | ResourceArtifact | Class | A sub type of ResourceArtifact that indicates a technology domain, i.e. nuclear, mechanical, electronic, mobile telephony etc. |
| TemporalPart | TemporalPart | MeasurableElement | Part | A current or future state of the wholeLifeEnterprise or another EnterprisePhase. |
| ToBeRealizedBy | ToBeRealizedBy |  | Dependency | Relation states that a functional or non-functional requirement should be realized through this element. |
| UAFElement | UAFElement |  |  | Abstract super type for all of the UAF elements. It provides a way for all of the UAF elements to have a common set of properties. |
| VersionedElement | VersionedElement | UAFElement |  | An abstract type grouping ResourcePerformer and ServiceSpecification that allows VersionOfConfiguration to be related to ActualProjectMilestones. |
| VersionOfConfiguration | VersionOfConfiguration | MeasurableElement | Part | A property of a WholeLifeConfiguration, used in version control of a VersionedElement. It asserts that a VersionedElement is a version of a WholeLifeConfigurati |
| VersionReleased | VersionReleased |  | Dependency | A relationship that expresses that an actual project milestone releases an versioned element. |
| VersionSuccession | VersionSucession | MeasurableElement | Dependency | A tuple between two VersionOfConfigurations that denotes that one VersionOfConfiguration follows from another. |
| VersionWithdrawn | VersionWithdrawn |  | Dependency | A relationship that expresses that an actual project milestone withdraws an versioned element. |
| View | View | PropertySet | Class | An architecture view expresses the architecture of the system-of-interest in accordance with an architecture viewpoint (or simply, viewpoint). [ISO/IEC/IEEE 420 |
| Viewpoint | Viewpoint | PropertySet | Class | An architecture viewpoint frames (to formulate or construct in a particular style or language) one or more concerns. A concern can be framed by more than one vi |
| ViewpointsInArchitecturalDescription | ViewpointsInArchitecturalDescription |  | Dependency | A relationship that expresses that an architectural description includes the following viewpoints. |
| ViewpointToStakeholder | ViewpointToStakeholder |  | Dependency | A relationship that expresses which stakeholder needs viewpoint. |
| ViewsInArchitecturalDescription | ViewsInArchitecturalDescription |  | Dependency | A relationship that expresses that an architectural description includes the following views. |
| VisionForActualEnterprisePhase | VisionForActualEnterprisePhase |  | Dependency | A relationship that expresses which actual enterprisephase implements an enterprisevision. |
| WholeLifeConfiguration | WholeLifeConfiguration | PropertySet | Class | A set of VersionedElements. |
| WholeLifeEnterprise | WholeLifeEnterprise | EnterprisePhase | Class | A WholeLifeEnterprise is a purposeful endeavor of any size involving people, organizations and supporting systems. It is made up of TemporalParts and Structural |
| A1 - Meta-Data Definitions |  |  | Diagram_Custom | Architectures, particularly large ones, usually require meta-data tags to aid with searching and discovery. |
| A2 - Architecture Products |  |  | Diagram_Custom | The A2 Viewpoint specifies the structure of an architecture, and the products that describe the architecture. Each product may correspond to an architecture vie |
| A3 - Architecture Correspondence |  |  | Diagram_Custom | ISO/IEC/IEEE42010 introduces the idea of architecture correspondence and correspondence rules. Quoting from ISO/IEC/IEEE 42010; “A correspondence defines a rela |
| A4 - Methodology Used |  |  | Diagram_Custom | The A4 Viewpoint specifies the methodology used for the architecting activities. This methodology is described in NAFv4 Chapter 2. The content of the A4 viewpoi |
| A5 - Architecture Status |  |  | Diagram_Custom | Since NAFv3.0, it has been possible to assign version numbers to views and specify their approval dates. In NAFv4.0, this is integrated with the meta-model’s ge |
| A6 - Architecture Version |  |  | Diagram_Custom | Where the A5 Viewpoint shows the current version number and approval status for the architecture, the A6 Viewpoint shows the complete history of the architectur |
| A7 - Architecture Compliance |  |  | Diagram_Custom | The A7 Viewpoint gives the overall specification of architecture meta-data. |
| A8 - Standards |  |  | Diagram_Custom | The A8 Viewpoint encompasses both technical and non-technical standards. The standards specified in the A8 view can be applied across the architecture to a vari |
| Ar - Architecture Roadmap |  |  | Diagram_Custom | The Ar Viewpoint shows the history of the architecture project as well as its future direction. |
| C1 - Capability Taxonomy |  |  | Diagram_Custom | The C1 Viewpoint specifies all the capabilities that are referenced throughout one or more architectures – i.e. one C1 may provide the definitive list of capabi |
| C2 - Enterprise Vision |  |  | Diagram_Custom | The purpose of the C2 Viewpoint is to provide a strategic context for the capabilities described in the architecture and to specify the scope for the architectu |
| C3 - Capability Dependencies |  |  | Diagram_Custom | The C3 Viewpoint is intended to provide a means of analysing the dependencies between capabilities and between capability clusters. The composition of capabilit |
| C4 - Standard Processes |  |  | Diagram_Custom | The C4 Viewpoint specifies Standard Operational Activities that can be re-used across multiple logical architectures (e.g. in L4, Logical Activities). |
| C5 - Effects |  |  | Diagram_Custom | The purpose of the C5 Viewpoint is to describe the operational effect of the capabilities, activities and services according to the expected goals. The C5 Viewp |
| C7 - Performance Parameters |  |  | Diagram_Custom | In the C7 Viewpoint the capability requirements (and existing capabilities) can be expressed in terms of Measures of Effectiveness (MoEs). These are high-level  |
| C8 - Planning Assumptions |  |  | Diagram_Custom | The C8 Viewpoint is concerned with identification and description of assumptions that have been made for the implementation of capabilities. Assumptions can be  |
| Cr - Capability Roadmap |  |  | Diagram_Custom | The Cr Viewpont supports the Capability Audit process by providing a method to identify gaps or duplications in capability provision. Cr indicates capability in |
| Business Process |  |  | Diagram_Analysis |  |
| L1 - Node Types |  |  | Diagram_Custom | The L1 Viewpoint defines all of the Nodes that will appear in a Logical Architecture. Nodes are elements of capability assembled and orchestrated in the Logical |
| L2 - Logical Scenario |  |  | Diagram_Custom | The L2 Viewpoint specifies Nodes (elements of capability) in context of each other. The context is usually expressed in terms of the information that flows betw |
| L3 - Node Interactions |  |  | Diagram_Custom | L3 is used to provide further detail of the interoperability requirements associated with the operational capability of interest. The focus is on logical flows  |
| L4 - Logical Activities |  |  | Diagram_Custom | The L4 Viewpoint describes the operational activities that are being conducted within the mission or scenario. These activities are defined at a logical, soluti |
| L5 - Logical States |  |  | Diagram_Custom | The L5 Viewpoint specifies the typical states a node may have and the possible transitions between those states (i.e. changes of state). Triggers for state chan |
| L6 - Logical Sequence |  |  | Diagram_Sequence | Operational Event-Trace Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between nodes in |
| L7 - Information Model |  |  | Diagram_Custom | The L7 Viewpoint is used to document the business information. It describes the information that can be exchanged along the logical flows in the architecture, s |
| L8 - Logical Constraints |  |  | Diagram_Custom | The L8 Viewpoint is used to constrain the logical architecture without forcing a particular solution. L8 is used for rules which are not expressed as behavioura |
| Lr - Lines of Development |  |  | Diagram_Custom | The Lr Viewpoint is primarily intended to support the acquisition process across multiple projects or programmes, highlighting dependencies the logical dependen |
| L2-L3 - Logical Concept |  |  | Diagram_Custom | The L2-L3 Viewpoint is concerned with providing an executive level, scenario-based communication of the architecture purpose, scope and content. |
| P1 - Resource Types |  |  | Diagram_Custom | The P1 Viewpoint collects together all the Resource Types in the architecture together with a depiction of their performance characteristics. P1 also provides a |
| P2 - Resource Structure |  |  | Diagram_Custom | The P2 Viewpoint links together the operational and physical architecture viewpoints by depicting how types of Resource are structured and interact to realize t |
| P3 - Resource Connectivity |  |  | Diagram_Custom | The networks and pathways documented in a P3 Viewpoint represent the physical implementation of the logical flows identified in a L2, Logical Scenario, or L3, N |
| P4 - Resource Functions |  |  | Diagram_Custom | The Functionality Description provides detailed information regarding the allocation of functions to resources, and flows between Resource Functions. The P4 Vie |
| P5 - Resource States |  |  | Diagram_Custom | The P5 Viewpoint identifies the states a Resource can be, the allowable changes between those states, and the stimuli (e.g. triggers and events) that cause the  |
| P6 - Resource Sequence |  |  | Diagram_Sequence | The P6 Viewpoint is valuable for moving to the next level of detail from the initial solution design, to help define a sequence of functions and Resource Intera |
| P7 - Data Model |  |  | Diagram_Custom | The P7 Viewpoint is one of the architectural products closest to actual system design in the NAF. It is used to describe how the information represented in the  |
| P8 - Resource Constraints |  |  | Diagram_Custom | The P8 Viewpoint describes constraints on the Resources, Resource Functions, data and communications that make up a Physical Architecture. |
| Pr - Configuration Management |  |  | Diagram_Custom | The Pr Viewpoint provides an overview of how Resource Assets change over time (note that NAF v3.1 only allowed for Capability Configurations whereas now this is |
| L4-P4 - Activity To Function Mapping |  |  | Diagram_Custom | The L4-P4 Viewpoint depicts the mapping of Resource Functions (and optionally, the resources that provide them) to operational activities and/or service functio |
| R2 - Requirement Catalogue |  |  | Diagram_Custom | The R2 represents a catalog of requirements in the architectural model. For this purpose, categories can be created in which the functional and non-functional r |
| R3 - Requirement Dependencies |  |  | Diagram_Custom | The R3 is used to show dependencies between different requirements. |
| R7 - Requirement Derivation |  |  | Diagram_Custom | The R7 assigns functional and non-functional requirements to the demanding architectural elements. In addition, information about the planned realization can be |
| R8 - Requirement Fulfilment |  |  | Diagram_Custom | The R8 is used to determine and map acceptance and evaluation criteria for the individual functional and non-functional requirements. |
| Rr - Requirement Realization |  |  | Diagram_Custom | In the Rr, requirements are assigned to the realizing architectural elements. |
| S1 - Service Taxonomy |  |  | Diagram_Custom | The purpose of the S1 Viewpoint is to provide a governance structure for a Service-Oriented Architecture. Along with S3, Service Interfaces, it specifies a stan |
| S2 - Service Structure |  |  | Diagram_Custom | The S2 Viewpoint is concerned with identification and description of how services are structured to create a higher-aggregated service. To provide highlevel vie |
| S3 - Service Interfaces |  |  | Diagram_Custom | The S3 Viewpoint is concerned with the identification and definition of service interfaces. |
| S4 - Service Functions |  |  | Diagram_Custom | The S4 Viewpoint is the key behavioural specification for services. Equivalent in nature to L4, Logical Activities and P4, Resources Functions, it specifies a s |
| S5 - Service States |  |  | Diagram_Custom | The S5 Viewpoint is a specification of the allowable states of a service, and the possible transitions between them. This specification constrains how implement |
| S6 - Service Interactions |  |  | Diagram_Sequence | Service Interaction Descriptions, sometimes called sequence diagrams, event scenarios or timing diagrams, allow the tracing of interactions between services in  |
| S7 - Service Interface Parameters |  |  | Diagram_Custom | Specifies the interfaces that a service provides and uses, defines which services are compatible with which other services. |
| S8 - Service Policy |  |  | Diagram_Custom | The S8 Viewpoint specifies constraints against services to which implementations must conform. |
| Sr - Service Roadmap |  |  | Diagram_Custom | The Sr Viewpoint supports the Service Audit process by providing a method to identify gaps or duplications in service provision. Sr indicates service lifetime e |
| C1-S1 - Capability to Service Mapping |  |  | Diagram_Custom | A C1-S1 Viewpoint presents a simple mapping of services to capabilities, showing which services contribute to which capability. |
| Foundation-Elements |  |  | ToolboxPage |  |
| Project for Architecture |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| A2-Concerns && Viewpoints |  |  | ToolboxPage |  |
| A2-Stakeholders |  |  | ToolboxPage |  |
| A2-Enterprise |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| A3-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Architecural Sequence && Roadmap |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| A7-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| A8-Elements |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| All Stereotypes |  |  | ToolboxPage |  |
| Ar-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| NAFv4-ADMBw-BusinessProcess-Toolbox::hidden |  |  | ToolboxPage |  |
| Process modeling |  |  | ToolboxPage |  |
| assign to Operational Agents / Service |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| ActsUpon  |  |  | ToolboxPage |  |
| Implement |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C1-S1-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C1-Elements && Relationships |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C2-EnduringTask |  |  | ToolboxPage |  |
| C2-Enterprise |  |  | ToolboxPage |  |
| C2-Exhibits |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Physical Architecture Of Enterprise Phase |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C3-Capability |  |  | ToolboxPage |  |
| C3-CapabilityRole |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C4-Maps To Capability |  |  | ToolboxPage |  |
| C4-EnduringTask |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C5-Desirer |  |  | ToolboxPage |  |
| C5-Actual State |  |  | ToolboxPage |  |
| C5-Relationships |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| C5-Achiever |  |  | ToolboxPage |  |
| C5-Achiever Types |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| C7-Measurements |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Strategic Constraints |  |  | ToolboxPage |  |
| Implements Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Catalogue management |  |  | ToolboxPage |  |
| Cr-Capability && Configuration |  |  | ToolboxPage |  |
| Cr-Project |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L1-Elements |  |  | ToolboxPage |  |
| L1-Relationships |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L2-L3-Elements |  |  | ToolboxPage |  |
| L2-L3-Relationships |  |  | ToolboxPage |  |
| L2-L3-Types |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L2-Elements |  |  | ToolboxPage |  |
| L2-Relationships |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Condition, Environment && Location |  |  | ToolboxPage |  |
| L2-Operational Exchange Items |  |  | ToolboxPage |  |
| L2-Operational Constraints |  |  |  |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L3-Nodes |  |  | ToolboxPage |  |
| L3-Node Relationships |  |  | ToolboxPage |  |
| L3-Activities |  |  | ToolboxPage |  |
| L3-OperationalExchangeItems |  |  | ToolboxPage |  |
| L3-Services |  |  | ToolboxPage |  |
| Condition, Environment && Location |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L4-P4-Relationships |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L4-OperationalElements |  |  | ToolboxPage |  |
| L4-Relationships |  |  | ToolboxPage |  |
| L4-ActsUpon |  |  | ToolboxPage |  |
| L4-Service |  |  | ToolboxPage |  |
| L4-Conditions |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| References |  |  | ToolboxPage |  |
| Implement |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L5-Elements |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L6-Elements && Relationships |  |  | ToolboxPage |  |
| L6-Interaction |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| L7-Elements && Relationships |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Implements Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Lr-Actual Projects |  |  | ToolboxPage |  |
| Lr-Project Definition |  |  | ToolboxPage |  |
| Architecture for Project |  |  | ToolboxPage |  |
| Operational Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P1-Elements && Relationships |  |  | ToolboxPage |  |
| P1-Forecast |  |  | ToolboxPage |  |
| P1-Organizations |  |  | ToolboxPage |  |
| P1-StoredIn |  |  | ToolboxPage |  |
| P1-Implements |  |  | ToolboxPage |  |
| P1-Services |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P2-Elements && Relationships |  |  | ToolboxPage |  |
| P2-Resource Exchange  |  |  | ToolboxPage |  |
| P2-Organizations |  |  | ToolboxPage |  |
| P2-Services |  |  | ToolboxPage |  |
| P2-Project && Resource |  |  | ToolboxPage |  |
| P2-Implements |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Environment && Location |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P3-Elements && Dependency |  |  | ToolboxPage |  |
| P3-Connector && ResourcePort |  |  | ToolboxPage |  |
| P3-Protocols |  |  | ToolboxPage |  |
| P3-Exchanges |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| P4-Functions |  |  | ToolboxPage |  |
| P4-Resource Function Mapping |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Affecte && Subject |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P5-Elements |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P6-Elements |  |  | ToolboxPage |  |
| P6-Interaction |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P7-Elements && Relationships |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| P8-Personnel |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Implements Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Successor of |  |  | ToolboxPage |  |
| Pr-Configuration Management |  |  | ToolboxPage |  |
| Pr-Project Management |  |  | ToolboxPage |  |
| Resource Constraints |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| R2-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| R3-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| R7-Elements && Relationships |  |  | ToolboxPage |  |
| Constraints && References |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| R8-Elements && Relationships |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Rr-Realise |  |  | ToolboxPage |  |
| Rr-Realizing Service |  |  | ToolboxPage |  |
| Rr-Realizing Resources |  |  | ToolboxPage |  |
| Rr-Realizing Organizations |  |  | ToolboxPage |  |
| Rr-Realizing Standards |  |  | ToolboxPage |  |
| Rr-Realizing Measurement |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S1-Elements && Relationships |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S2-Service |  |  | ToolboxPage |  |
| S2-Dependency to Operational Agent |  |  | ToolboxPage |  |
| S2-Dependency to Resources |  |  | ToolboxPage |  |
| S2-Interface |  |  | ToolboxPage |  |
| S2-ServiceFunction |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S3-Elements && Relationships |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S4-Elements && Relationships |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S5-Elements |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S6-Elements && Relationships |  |  | ToolboxPage |  |
| S6-Interaction |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| S7-Elements && Relationships |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Service Policy |  |  | ToolboxPage |  |
| Implements Constraints |  |  | ToolboxPage |  |
| Measurements |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |
| Sr-Project |  |  | ToolboxPage |  |
| Sr-Services |  |  | ToolboxPage |  |
| Conforms To Standard |  |  | ToolboxPage |  |
| Findings && Recommendations |  |  | ToolboxPage |  |