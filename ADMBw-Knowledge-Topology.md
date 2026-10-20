# ADMBw-Topologie-Regeln (MDG-Metaconstraints)

> Quelle: `NAFv4-ADMBw-MDG-2026.05.xml` — automatisch erzeugt (ohne Zeitstempel)
> 203 Stereotype mit Beziehungsregeln (Metaconstraints) · 133 vollständig (Quelle und Ziel)

## Lesart

- **Quelle:** client, source, end[0].role oder informationSource — je nach UML-Metaklasse.
- **Ziel:** supplier, target, end[1].role oder informationTarget — je nach UML-Metaklasse.
- **Weitere Rollen:** zusätzliche Metamodell-Beschränkungen (Rollennamen direkt aus der MDG).
- **Vollständigkeit:** Nur Regeln mit Quelle **und** Ziel (133 von 203) sind maschinell prüfbar; Regeln mit ausschließlich „Weiteren Rollen“ dienen als Referenz.
- **Abstrakte Typen:** Endpunkte, die auf abstrakte Stereotype verweisen (🔒), gelten für alle konkreten Subtypen. Die Auflösung steht unten unter „Abstrakte Endpunkte“.

| Stereotype | Erlaubte Quellen (client/source/end[0]) | Erlaubte Ziele (supplier/target/end[1]) | Weitere Rollen |
|---|---|---|---|
| AchievedEffect | Achiever | ActualState |  |
| ActivityPerformableUnderCondition | BusinessProcess | ActualCondition |  |
| ActivitySupportsService | OperationalActivity | ServiceSpecification |  |
| ActsUpon | OperationalActivity, OperationalActivityAction | OperationalExchangeItem, PaperForm |  |
| ActualCondition |  |  | classifier → Condition |
| ActualConditionToActualResource | ActualResource | ActualCondition |  |
| ActualEnduringTask |  |  | classifier → EnduringTask |
| ActualEnterprisePhase |  |  | classifier → EnterprisePhase |
| ActualEnvironment |  |  | classifier → Environment |
| ActualLocation |  |  | classifier → Location |
| ActualMeasurement |  |  | definingFeature → Measurement, owningInstance → ActualPropertySet |
| ActualMeasurementSetAppliesFor | ActualMeasurementSet | MeasurableElement |  |
| ActualOrganization |  |  | classifier → Organization |
| ActualOrganizationRole |  |  | definingFeature → PostRole, definingFeature → SubOrganization, owningInstance → ActualOrganization |
| ActualPerson |  |  | classifier → Person |
| ActualPost |  |  | classifier → Post |
| ActualProject |  |  | classifier → Project, definingFeature → ProjectRole |
| ActualProjectConsults | ActualProject | Organization |  |
| ActualProjectDependency | ActualProject | ActualProject |  |
| ActualProjectInforms | ActualProject | Organization |  |
| ActualProjectMilestone |  |  | classifier → ProjectMilestone |
| ActualProjectMilestoneRole |  |  | definingFeature → ProjectMilestoneRole, owningInstance → ActualProject, value.instance → ActualProjectMilestone |
| ActualPropertySet |  |  | classifier → PropertySet |
| ActualResource |  |  | classifier → ResourcePerformer |
| ActualResourceNeededByActualProjectMilestone | ActualResource | ActualProjectMilestone |  |
| ActualResourceRelationship | ActualResource | ActualResource | realizes → ResourceExchange |
| ActualResourceRole |  |  | definingFeature → ResourceRole, owningInstance → ActualResource |
| ActualResourceToActualProjectMilestone | ActualResource | ActualProjectMilestone |  |
| ActualService |  |  | classifier → ServiceSpecification |
| ActualServiceSpecificationRole |  |  | definingFeature → ServiceSpecificationRole, owningInstance → ActualService |
| AffectedActivity | OperationalExchangeItem | OperationalActivity |  |
| AffectedFunctions | ResourceExchangeItem | Function |  |
| AffectedResource | OperationalActivity | OperationalExchangeItem |  |
| AlignsWithGoal | OperationalActivity, OperationalAgent, ResourcePerformer, ServiceSpecification | EnterpriseGoal |  |
| ArbitraryConnector | ConceptRole | ConceptRole |  |
| ArchitecturalReference | ArchitecturalDescription | ArchitecturalDescription |  |
| ArchitecturalSequence | ArchitecturalDescription | ArchitecturalDescription |  |
| ArchitectureForProject | ActualProject, ActualProjectMilestone | ArchitecturalDescription |  |
| ArchitectureMetadata |  |  | annotatedElement → ArchitecturalDescription |
| BoundaryCondition | ResourceConnector | Environment |  |
| CapabilityDependency | Capability | Capability |  |
| CapabilityForTask | Capability | ActualEnduringTask, EnduringTask |  |
| CapabilityGeneralization | Capability | Capability |  |
| CapabilityRole |  |  | class → Capability, type → Capability |
| CapabilityRoleDependency | CapabilityRole | CapabilityRole |  |
| Checks | FitCriterion | BWRequirement |  |
| Classified | ArchitecturalDescription, DataElement, DocumentReference, InformationElement, ServiceSpecification | Classification |  |
| Command | OrganizationalResource, ResourceRole | OrganizationalResource, ResourceRole | conveyed → DataElement |
| CompetenceForRole | ResourceRole | Competence |  |
| CompliesViewpoint | View | Viewpoint |  |
| ConceptRole |  |  | class → HighLevelOperationalConcept, type → ConceptItem |
| ConcernForActualEnterprisePhase | ActualEnterprisePhase | Concern |  |
| ConcernForView | View | Concern |  |
| ConcernForViewpoint | Viewpoint | Concern |  |
| ConflictsWith | BWRequirement | BWRequirement |  |
| ConformsTo | UAFElement | Standard |  |
| ConsumedBy | ServiceSpecification, ServiceSpecificationRole | OperationalPerformer, OperationalRole |  |
| Consumes | OperationalActivity, OperationalActivityAction | ActualService, ServiceSpecification |  |
| Control | PhysicalResource, ResourceRole | PhysicalResource, ResourceRole | conveyed → DataElement |
| DataElement |  |  | owner → DataModel |
| DataElementStoredIn | DataElement | ResourcePerformer, ResourceRole |  |
| DataRole |  |  | class → ResourceAsset, type → DataElement |
| DerivedFrom | BWRequirement | UAFElement |  |
| DescribedBy | Architecture | ArchitecturalDescription |  |
| DesiredEffect | Desirer | ActualState |  |
| EnvironmentalCondition | Exhibits | Environment |  |
| EnvironmentalContext | Measurement | ActualCondition |  |
| EnvironmentProperty |  |  | class → Environment, type → Condition |
| Evaluates | FulfilmentCriterion | FitCriterion |  |
| Exhibits | CapableElement | Capability |  |
| Expresses | Architecture | ArchitecturalDescription |  |
| FieldedCapability |  |  | classifier → CapabilityConfiguration |
| FillsPost | ActualPerson | ActualPost |  |
| Forecast | SubjectOfForecast | SubjectOfForecast |  |
| ForecastPeriod | Forecast | ActualEnterprisePhase |  |
| FormStoredIn | PaperForm | Software |  |
| FunctionAction |  |  | activity → Function, behavior → Function |
| FunctionControlFlow | ActivityInitial, DecisionNode, ForkNode, FunctionAction, JoinNode, MergeNode | ActivityFinal, DecisionNode, FlowFinal, ForkNode, FunctionAction, JoinNode, MergeNode |  |
| FunctionEdge |  |  | owner → Function |
| FunctionObjectFlow | ActivityInitial, DecisionNode, ForkNode, FunctionAction, JoinNode, MergeNode | ActivityFinal, DecisionNode, FlowFinal, ForkNode, FunctionAction, JoinNode, MergeNode |  |
| FunctionSubject | Function | ResourceExchangeItem |  |
| GoalForActualEnterprisePhase | ActualEnterprisePhase | EnterpriseGoal |  |
| HostedOn | ResourceArchitecture, ResourceArtifact, ResourceRole | ResourceArchitecture, ResourceArtifact, ResourceRole |  |
| Implements | DataElement, Function, InformationElement, OperationalActivity, OperationalActivityAction, OperationalConstraint, ResourceConnector, ResourceConstraint, ResourceExchange, ResourceInterface, ResourcePerformer, ResourceRole, ServicePolicy, StrategicConstraint | ActualEnduringTask, InformationElement, OperationalActivity, OperationalActivityAction, OperationalAgent, OperationalConnector, OperationalConstraint, OperationalExchange, OperationalInterface, OperationalRole, ResourceConnector, ResourceConstraint, ServiceFunction, ServiceInterface, ServicePolicy, StrategicConstraint |  |
| ImplementsProtocol | ProtocolImplementation | Protocol |  |
| Information |  |  | annotatedElement → UAFElement |
| InformationElement |  |  | owner → DataModel |
| InformationRole |  |  | class → OperationalAsset, type → InformationElement |
| IsAccountableFor | Organization | ActualProject, ResourcePerformer, ServiceSpecification |  |
| IsCapableToPerform | OperationalAgent, ResourcePerformer, ServiceSpecification | Function, FunctionAction, Lane, OperationalActivity, OperationalActivityAction, Pool, ServiceFunction, ServiceFunctionAction |  |
| IsDuplicateOf | BWRequirement | BWRequirement |  |
| IsEquivalentToStandardElement | UAFElement | UAFElement |  |
| IsResponsibleFor | Organization | ActualProject, ResourcePerformer, ServiceSpecification |  |
| JustifiedBy | OperationalConstraint, ResourceConstraint, ServicePolicy, StrategicConstraint | Reference |  |
| LocationType | LocationHolder | Location |  |
| MapsToCapability | BusinessProcess | Capability |  |
| Measurement |  |  | class → PropertySet, type → MeasurementType |
| Metadata |  |  | annotatedElement → UAFElement |
| MilestoneDependency | ActualProjectMilestone | ActualProjectMilestone |  |
| NeedsModificationOf | ActualProject | PhysicalResource, ResourceArchitecture, ResourceRole |  |
| NeedsResource | ActualProject | PhysicalResource, ResourceArchitecture, ResourceRole |  |
| NeedsService | ActualProject | ServiceSpecification, ServiceSpecificationRole |  |
| OperationalActivity |  |  | ownedParameter → OperationalParameter |
| OperationalActivityAction |  |  | activity → OperationalActivity, behavior → OperationalActivity |
| OperationalActivityEdge |  |  | owner → OperationalActivity |
| OperationalAgent |  |  | ownedOperation → OperationalMethod, ownedPort → OperationalPort |
| OperationalArchitectureOfEnterprisePhase | ActualEnterprisePhase | OperationalArchitecture |  |
| OperationalConnector | OperationalPort, OperationalRole | OperationalPort, OperationalRole |  |
| OperationalControlFlow | Gateway, IntermediateEvent, OperationalActivityAction, StartEvent | EndEvent, Gateway, IntermediateEvent, OperationalActivityAction |  |
| OperationalExchange | OperationalActivity, OperationalAgent, OperationalRole, ServiceSpecification | OperationalActivity, OperationalAgent, OperationalRole, ServiceSpecification | conveyed → OperationalExchangeItem, realizingActivityEdge → OperationalActivityEdge, realizingConnector → OperationalConnector, realizingMessage → OperationalMessage |
| OperationalMessage |  |  | receiveEvent.event.operation → OperationalMethod |
| OperationalMessageFlow | IntermediateEvent, Lane, OperationalActivityAction, Pool | IntermediateEvent, Lane, OperationalActivityAction, Pool |  |
| OperationalMethod |  |  | method → OperationalActivity, ownedOperation → OperationalInterface, ownedParameter → OperationalParameter |
| OperationalObjectFlow | Gateway, IntermediateEvent, OperationalActivityAction, StartEvent | EndEvent, Gateway, IntermediateEvent, OperationalActivityAction |  |
| OperationalParameter |  |  | type → OperationalExchangeItem |
| OperationalPort |  |  | class → OperationalAgent, type → OperationalInterface |
| OperationalRole |  |  | class → OperationalAgent, class → OperationalArchitecture, class → OperationalPerformer, type → KnownResource, type → OperationalAgent, type → OperationalArchitecture, type → OperationalPerformer |
| OperationalSignalProperty |  |  | class → OperationalSignal, type → OperationalExchangeItem |
| OperationalStateDescription |  |  | owner → OperationalAgent |
| OriginatesFrom | UAFElement | Reference |  |
| OwnedMilestone | ActualProject | ActualProjectMilestone |  |
| OwnsActualMeasurementSet | MeasurableElement | ActualMeasurementSet |  |
| OwnsMeasurement | MeasurableElement | Measurement, MeasurementType |  |
| OwnsProcess | ActualOrganizationalResource | OperationalActivity |  |
| PartOfCatalogue | RequirementCategory | RequirementCatalogue |  |
| PartOfCategory | BWRequirement, RequirementCategory | RequirementCategory |  |
| PerformsInContext | OperationalRole, ResourceRole, ServiceSpecificationRole | Function, FunctionAction, Lane, OperationalActivity, OperationalActivityAction, Pool, ServiceFunction, ServiceFunctionAction |  |
| PhysicalArchitectureOfEnterprisePhase | ActualEnterprisePhase | ResourceArchitecture |  |
| PhysicalLocation | LocationHolder | ActualLocation |  |
| PostRole |  |  | class → Organization, class → Post, type → Post |
| ProblemDomain |  |  | class → OperationalArchitecture, type → OperationalPerformer |
| ProcessGeneralization | BusinessProcess | BusinessProcess |  |
| ProjectMilestoneRole |  |  | class → Project, type → ProjectMilestone |
| ProjectMilestoneToProjectTheme | ProjectMilestone | ProjectTheme |  |
| ProjectProvidesFunction | ActualProject | Function |  |
| ProjectRole |  |  | class → Project, type → Project |
| ProjectSequence | ActualProject | ActualProject |  |
| ProjectStatus |  |  | definingFeature → ProjectTheme |
| ProjectSupportActivity | ActualProject | OperationalActivity |  |
| PropertySetGeneralization | CapabilityConfiguration, PropertySet, System | CapabilityConfiguration, PropertySet, System |  |
| ProtocolLayer |  |  | class → Protocolstack, type → Protocol |
| Provides | OperationalPerformer, OperationalRole | ServiceSpecification, ServiceSpecificationRole |  |
| ProvidesCompetence | ActualOrganizationalResource | Competence |  |
| ProvidesServiceFunction | ServiceInterface | ServiceFunction |  |
| RatifiedStandards | ActualOrganization | Standard |  |
| RealiseRequirement | DataElement, Function, Measurement, MeasurementType, Protocol, Protocolstack, ResourcePerformer, ResourcePort, ResourceRole, ServiceFunction, ServiceInterface, ServiceSpecification, ServiceSpecificationRole, Standard | BWRequirement |  |
| RealizedDesiredEffect | AchievedEffect | DesiredEffect |  |
| RealizesRecommendation | UAFElement | Recommendation |  |
| RealizingAchievedEffect | DesiredEffect | AchievedEffect |  |
| RefersTo | Recommendation | Finding |  |
| Refines | BWRequirement | BWRequirement |  |
| Replaces | BWRequirement | BWRequirement |  |
| ReplaceStandardElement | Reference, UAFElement | Reference, UAFElement |  |
| RequiredEnvironment | LocationHolder | ActualEnvironment |  |
| RequiredResource | ProjectMilestone | ResourcePerformer |  |
| Requires | BWRequirement | BWRequirement |  |
| RequiresCompetence | OrganizationalResource | Competence |  |
| ResourceConnector | ResourcePort, ResourceRole | ResourcePort, ResourceRole |  |
| ResourceDependency | ResourcePerformer, ResourcePort, ResourceRole | ResourcePerformer, ResourcePort, ResourceRole |  |
| ResourceExchange | ResourcePerformer, ResourceRole, ServiceSpecificationRole | ResourcePerformer, ResourceRole, ServiceSpecificationRole | conveyed → ResourceExchangeItem, realizingActivityEdge → FunctionEdge, realizingConnector → ResourceConnector, realizingMessage → ResourceMessage |
| ResourceMessage |  |  | Connector → ResourceConnector, receiveEvent.event.operation → ResourceMethod |
| ResourceMethod |  |  | method → Function, ownedOperation → ResourceInterface, ownedOperation → ResourcePerformer, ownedParameter → ResourceParameter |
| ResourceParameter |  |  | ownedParameter → Function, type → ResourceExchangeItem |
| ResourcePerformer |  |  | ownedPort → ResourcePort |
| ResourcePort |  |  | class → ResourcePerformer, type → ResourceInterface |
| ResourceRole |  |  | class → ResourcePerformer, type → ResourcePerformer |
| ResourceSignalProperty |  |  | class → ResourceSignal, type → ResourceExchangeItem |
| ResourceStateDescription |  |  | owner → ResourcePerformer |
| ResourceToServiceDependency | ResourcePerformer, ResourceRole | ServiceSpecification, ServiceSpecificationRole |  |
| Responsible | ActualProject | PhysicalResource, ResourceArchitecture, ResourceRole, ServiceSpecification |  |
| ResultsFrom | Finding | Classification, EndEvent, FitCriterion, FulfilmentCriterion, FunctionalRequirement, Gateway, IntermediateEvent, Lane, Measurement, MeasurementType, NonfunctionalRequirement, Pool, Reference, RequirementCatalogue, RequirementCategory, StartEvent, UAFElement |  |
| SameAs | Software, UAFElement | Software, UAFElement |  |
| Satisfy | Capability, OperationalActivityAction, ServiceSpecification, SubjectOfOperationalConstraint, SubjectOfResourceConstraint | OperationalConstraint, ResourceConstraint, ServicePolicy, StrategicConstraint |  |
| SecurityConstraint |  |  | constrainedElement → SubjectOfSecurityConstraint |
| ServiceConnector | ServicePort, ServiceSpecificationRole | ServicePort, ServiceSpecificationRole |  |
| ServiceDependency | ServiceSpecification | OperationalAgent, ResourcePerformer, ServiceSpecification |  |
| ServiceExchange | ServiceSpecification | ServiceSpecification | realizingConnector → ServiceConnector, realizingMessage → ServiceMessage |
| ServiceFunction |  |  | ownedParameter → ServiceParameter |
| ServiceFunctionAction |  |  | activity → ServiceFunction, behavior → ServiceFunction |
| ServiceGeneralization | ServiceSpecification | ServiceSpecification |  |
| ServiceInterface |  |  | ownedOperation → ServiceMethod |
| ServiceMethod |  |  | method → ServiceFunction, ownedParameter → ServiceParameter, receiveEvent.event.operation → ServiceMessage |
| ServiceParameter |  |  | type → OperationalExchangeItem |
| ServicePort |  |  | class → ServiceSpecification, type → ServiceInterface |
| ServiceProvision | ActualResource, ResourcePerformer, ResourceRole | ActualService, ServiceSpecification, ServiceSpecificationRole |  |
| ServiceSpecification |  |  | ownedOperation → ServiceMethod, ownedPort → ServicePort |
| ServiceSpecificationRole |  |  | class → ServiceSpecification, type → ServiceSpecification |
| ServiceStateDescription |  |  | owner → ServiceSpecification |
| StakeholderConcern | Stakeholder | Concern |  |
| StatementTask | ActualEnterprisePhase | ActualEnduringTask |  |
| StemsFrom | BWRequirement | BWRequirement |  |
| SubOrganization |  |  | class → Organization, type → Organization |
| SuccessorOf | ResourcePerformer, ServiceSpecification, Standard | ResourcePerformer, ServiceSpecification, Standard |  |
| TemporalPart |  |  | class → EnterprisePhase, type → EnterprisePhase |
| ToBeRealizedBy | BWRequirement | DataElement, Function, Measurement, MeasurementType, Protocol, Protocolstack, ResourcePerformer, ResourcePort, ResourceRole, ServiceFunction, ServiceInterface, ServiceSpecification, ServiceSpecificationRole, Standard |  |
| VersionOfConfiguration |  |  | class → WholeLifeConfiguration, type → VersionedElement |
| VersionReleased | ActualProjectMilestone | VersionedElement |  |
| VersionSuccession | VersionOfConfiguration | VersionOfConfiguration |  |
| VersionWithdrawn | ActualProjectMilestone | VersionedElement |  |
| ViewpointsInArchitecturalDescription | ArchitecturalDescription | Viewpoint |  |
| ViewpointToStakeholder | Viewpoint | Stakeholder |  |
| ViewsInArchitecturalDescription | ArchitecturalDescription | View |  |
| VisionForActualEnterprisePhase | ActualEnterprisePhase | EnterpriseVision |  |

## Abstrakte Endpunkte

Diese Typen dürfen **nicht instanziiert** werden. Für die Prüfung eines konkreten Modells sind sie auf die aufgeführten konkreten Subtypen aufzulösen.

| Abstrakter Typ | Konkrete Subtypen |
|---|---|
| 🔒 Achiever | ActualEnterprisePhase, ActualOrganization, ActualPerson, ActualPost, ActualProject, ActualResource, FieldedCapability, Function, OperationalActivity, SecurityProcess, ServiceFunction, ServiceSpecification, StandardOperationalActivity |
| 🔒 ActualOrganizationalResource | ActualOrganization, ActualPerson, ActualPost, ActualProject |
| 🔒 ActualState | ActualCondition, ActualEnduringTask, ActualEnterprisePhase, ActualEnvironment, ActualLocation, ActualMeasurement, ActualMeasurementSet, ActualOrganization, ActualPerson, ActualPost, ActualProject, ActualProjectMilestone, ActualProjectMilestoneRole, ActualPropertySet, ActualResource, ActualService, FieldedCapability, ProjectStatus, ProvidedServiceLevel, RequiredServiceLevel |
| 🔒 Architecture | CapabilityConfiguration, OperationalArchitecture, ResourceArchitecture, ResourceMitigation, SecurityEnclave, System |
| 🔒 BWRequirement | FunctionalRequirement, NonfunctionalRequirement |
| 🔒 BusinessProcess | Function, OperationalActivity, SecurityProcess, ServiceFunction, StandardOperationalActivity |
| 🔒 CapableElement | ActualEnduringTask, ActualEnterprisePhase, ActualOrganization, ActualPerson, ActualPost, ActualProject, ActualResource, ActualService, CapabilityConfiguration, Energy, FieldedCapability, KnownResource, NaturalResource, OperationalArchitecture, OperationalPerformer, Organization, Person, Post, Project, ProvidedServiceLevel, RequiredServiceLevel, ResourceArchitecture, ResourceArtifact, ResourceMitigation, Responsibility, SecurityEnclave, ServiceSpecification, Software, System, Technology |
| 🔒 Desirer | Capability, CapabilityConfiguration, CapabilityRole, Energy, KnownResource, NaturalResource, OperationalArchitecture, OperationalPerformer, Organization, Person, Post, Project, ResourceArchitecture, ResourceArtifact, ResourceMitigation, Responsibility, SecurityEnclave, Software, System, Technology |
| 🔒 LocationHolder | CapabilityConfiguration, DataElement, Energy, InformationElement, KnownResource, NaturalResource, OperationalArchitecture, OperationalPerformer, OperationalRole, Organization, Person, Post, PostRole, ProblemDomain, Project, ProjectRole, ResourceArchitecture, ResourceArtifact, ResourceMitigation, ResourceRole, Responsibility, SecurityEnclave, Software, SubOrganization, System, Technology |
| 🔒 MeasurableElement | AchievedEffect, ActivityPerformableUnderCondition, Alias, ArbitraryConnector, ArchitecturalDescription, ArchitecturalReference, ArchitecturalSequence, ArchitectureMetadata, Capability, CapabilityConfiguration, CapabilityDependency, CapabilityForTask, CapabilityGeneralization, CapabilityRole, CapabilityRoleDependency, Command, Competence, ConceptRole, Concern, Condition, Consumes, Control, DataElement, DataRole, Definition, DesiredEffect, EnduringTask, Energy, EnterpriseGoal, EnterprisePhase, EnterpriseVision, Environment, EnvironmentProperty, Exhibits, FillsPost, Forecast, Function, FunctionAction, FunctionControlFlow, FunctionObjectFlow, GeoPoliticalExtentType, HighLevelOperationalConcept, Implements, Information, InformationElement, InformationRole, IsCapableToPerform, KnownResource, Location, MapsToCapability, Measurement, Metadata, MilestoneDependency, NaturalResource, OperationalActivity, OperationalActivityAction, OperationalArchitecture, OperationalConnector, OperationalConstraint, OperationalControlFlow, OperationalExchange, OperationalInterface, OperationalMessage, OperationalMethod, OperationalObjectFlow, OperationalParameter, OperationalPerformer, OperationalPort, OperationalRole, OperationalSignal, OperationalSignalProperty, OperationalStateDescription, Organization, OwnsProcess, PerformsInContext, Person, Post, PostRole, ProblemDomain, ProcessGeneralization, Project, ProjectMilestone, ProjectMilestoneRole, ProjectRole, ProjectSequence, ProjectTheme, PropertySetGeneralization, Protocol, ProtocolLayer, Protocolstack, ProvidesCompetence, RequiresCompetence, ResourceArchitecture, ResourceArtifact, ResourceConnector, ResourceConstraint, ResourceExchange, ResourceInterface, ResourceMessage, ResourceMethod, ResourceMitigation, ResourceParameter, ResourcePort, ResourceRole, ResourceSignal, ResourceSignalProperty, ResourceStateDescription, Responsibility, SameAs, SecurityConstraint, SecurityEnclave, SecurityProcess, ServiceConnector, ServiceExchange, ServiceFunction, ServiceFunctionAction, ServiceGeneralization, ServiceInterface, ServiceMessage, ServiceMethod, ServiceParameter, ServicePolicy, ServicePort, ServiceProvision, ServiceSpecification, ServiceSpecificationRole, ServiceStateDescription, Software, Standard, StandardOperationalActivity, StrategicConstraint, SubOrganization, System, Technology, TemporalPart, VersionOfConfiguration, VersionSuccession, View, Viewpoint, WholeLifeConfiguration, WholeLifeEnterprise |
| 🔒 OperationalAgent | KnownResource, OperationalArchitecture, OperationalPerformer |
| 🔒 OperationalExchangeItem | CapabilityConfiguration, Energy, GeoPoliticalExtentType, InformationElement, InformationRole, KnownResource, NaturalResource, OperationalSignal, Organization, Person, Post, Project, ResourceArchitecture, ResourceArtifact, ResourceMitigation, Responsibility, SecurityEnclave, Software, System, Technology |
| 🔒 OrganizationalResource | Organization, Person, Post, Project, Responsibility |
| 🔒 PhysicalResource | Energy, NaturalResource, Organization, Person, Post, Project, ResourceArtifact, Responsibility, Software, Technology |
| 🔒 PropertySet | Capability, CapabilityConfiguration, CapabilityRole, Competence, Concern, Condition, DataElement, DataRole, EnduringTask, Energy, EnterpriseGoal, EnterprisePhase, EnterpriseVision, Environment, GeoPoliticalExtentType, HighLevelOperationalConcept, InformationElement, InformationRole, KnownResource, Location, NaturalResource, OperationalArchitecture, OperationalInterface, OperationalPerformer, OperationalSignal, Organization, Person, Post, Project, ProjectMilestone, Protocol, Protocolstack, ResourceArchitecture, ResourceArtifact, ResourceInterface, ResourceMitigation, ResourceSignal, Responsibility, SecurityEnclave, ServiceInterface, ServiceSpecification, Software, Standard, System, Technology, TemporalPart, View, Viewpoint, WholeLifeConfiguration, WholeLifeEnterprise |
| 🔒 ProtocolImplementation | ResourceConnector, ResourcePort |
| 🔒 ResourceExchangeItem | CapabilityConfiguration, DataElement, DataRole, Energy, GeoPoliticalExtentType, KnownResource, NaturalResource, Organization, Person, Post, Project, ResourceArchitecture, ResourceArtifact, ResourceMitigation, ResourceSignal, Responsibility, SecurityEnclave, Software, System, Technology |
| 🔒 ResourcePerformer | CapabilityConfiguration, Energy, KnownResource, NaturalResource, Organization, Person, Post, Project, ResourceArchitecture, ResourceArtifact, ResourceMitigation, Responsibility, SecurityEnclave, Software, System, Technology |
| 🔒 Stakeholder | ActualOrganization, ActualPerson, ActualPost, ActualProject, Organization, Person, Post, Project, Responsibility |
| 🔒 SubjectOfForecast | CapabilityConfiguration, Competence, DataElement, Energy, InformationElement, KnownResource, NaturalResource, OperationalArchitecture, OperationalPerformer, Organization, Person, Post, Project, Protocol, Protocolstack, ResourceArchitecture, ResourceArtifact, ResourceMitigation, Responsibility, SecurityEnclave, Software, Standard, System, Technology |
| 🔒 SubjectOfOperationalConstraint | DataModel, DataRole, InformationElement, InformationRole, KnownResource, OperationalActivity, OperationalArchitecture, OperationalExchange, OperationalPerformer, OperationalRole, OperationalSignal, PostRole, ProblemDomain, ProjectRole, ResourceRole, SecurityProcess, StandardOperationalActivity, SubOrganization |
| 🔒 SubjectOfResourceConstraint | ActualOrganization, ActualPerson, ActualPost, ActualProject, ActualResource, CapabilityConfiguration, DataElement, DataModel, Energy, FieldedCapability, Function, KnownResource, NaturalResource, Organization, Person, Post, PostRole, Project, ProjectRole, ResourceArchitecture, ResourceArtifact, ResourceMitigation, ResourcePort, ResourceRole, Responsibility, SecurityEnclave, SecurityProcess, Software, SubOrganization, System, Technology |
| 🔒 UAFElement | AchievedEffect, ActivityPerformableUnderCondition, ActualCondition, ActualEnduringTask, ActualEnterprisePhase, ActualEnvironment, ActualLocation, ActualMeasurement, ActualMeasurementSet, ActualOrganization, ActualOrganizationRole, ActualPerson, ActualPost, ActualProject, ActualProjectMilestone, ActualProjectMilestoneRole, ActualPropertySet, ActualResource, ActualResourceRelationship, ActualResourceRole, ActualService, Alias, ArbitraryConnector, ArchitecturalDescription, ArchitecturalReference, ArchitecturalSequence, ArchitectureMetadata, Capability, CapabilityConfiguration, CapabilityDependency, CapabilityForTask, CapabilityGeneralization, CapabilityRole, CapabilityRoleDependency, Command, Competence, ConceptRole, Concern, Condition, Consumes, Control, DataElement, DataModel, DataRole, Definition, DesiredEffect, EnduringTask, Energy, EnterpriseGoal, EnterprisePhase, EnterpriseVision, Environment, EnvironmentProperty, Exhibits, FieldedCapability, FillsPost, Forecast, Function, FunctionAction, FunctionControlFlow, FunctionObjectFlow, GeoPoliticalExtentType, HighLevelOperationalConcept, Implements, Information, InformationElement, InformationRole, IsCapableToPerform, KnownResource, Location, MapsToCapability, Measurement, Metadata, MilestoneDependency, NaturalResource, OperationalActivity, OperationalActivityAction, OperationalArchitecture, OperationalConnector, OperationalConstraint, OperationalControlFlow, OperationalExchange, OperationalInterface, OperationalMessage, OperationalMethod, OperationalObjectFlow, OperationalParameter, OperationalPerformer, OperationalPort, OperationalRole, OperationalSignal, OperationalSignalProperty, OperationalStateDescription, Organization, OwnsProcess, PerformsInContext, Person, Post, PostRole, ProblemDomain, ProcessGeneralization, Project, ProjectMilestone, ProjectMilestoneRole, ProjectRole, ProjectSequence, ProjectStatus, ProjectTheme, PropertySetGeneralization, Protocol, ProtocolLayer, Protocolstack, ProvidedServiceLevel, ProvidesCompetence, RequiredServiceLevel, RequiresCompetence, ResourceArchitecture, ResourceArtifact, ResourceConnector, ResourceConstraint, ResourceExchange, ResourceInterface, ResourceMessage, ResourceMethod, ResourceMitigation, ResourceParameter, ResourcePort, ResourceRole, ResourceSignal, ResourceSignalProperty, ResourceStateDescription, Responsibility, SameAs, SecurityConstraint, SecurityEnclave, SecurityProcess, ServiceConnector, ServiceExchange, ServiceFunction, ServiceFunctionAction, ServiceGeneralization, ServiceInterface, ServiceMessage, ServiceMethod, ServiceParameter, ServicePolicy, ServicePort, ServiceProvision, ServiceSpecification, ServiceSpecificationRole, ServiceStateDescription, Software, Standard, StandardOperationalActivity, StrategicConstraint, SubOrganization, System, Technology, TemporalPart, VersionOfConfiguration, VersionSuccession, View, Viewpoint, WholeLifeConfiguration, WholeLifeEnterprise |
| 🔒 VersionedElement | CapabilityConfiguration, Energy, KnownResource, NaturalResource, Organization, Person, Post, Project, ResourceArchitecture, ResourceArtifact, ResourceMitigation, Responsibility, SecurityEnclave, ServiceSpecification, Software, System, Technology |