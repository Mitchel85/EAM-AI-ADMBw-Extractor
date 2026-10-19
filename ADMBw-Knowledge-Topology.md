# ADMBw-Topologie-Regeln (MDG-Metaconstraints)

> Quelle: `/root/hermes-workspace/architektur-mate-ki/tools/NAFv4-ADMBw-MDG-2026.05.xml` — automatisch erzeugt am 2026-10-19 05:34 UTC
> 203 Stereotype mit Metaconstraints · 133 vollständig (Quelle+Ziel) · 70 nur Rollen-Beschränkungen

## Lesart

- **Quelle:** client, source, end[0].role oder informationSource — je nach UML-Metaklasse.
- **Ziel:** supplier, target, end[1].role oder informationTarget — je nach UML-Metaklasse.
- **Nur Zeilen mit beiden Enden sind Kanten-Regeln.** Zeilen mit leeren Quellen-/Zielspalten enthalten ausschließlich Rollen-/Metamodell-Beschränkungen — sie definieren KEINE erlaubte Kante.
- **Exakter Namens-Match:** Source- und Target-Stereotype müssen stringgleich mit den Quellen-/Zielspalten übereinstimmen. Abstrakte Basisklassen (🔒) gelten nicht als konkreter Nachweis — die Kante ist dann FAIL.

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
