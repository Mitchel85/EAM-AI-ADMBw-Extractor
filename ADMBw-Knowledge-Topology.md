# ADMBw-Topologie-Regeln (MDG-Metaconstraints)

> Quelle: `/tmp/NAFv4-ADMBw-MDG-2026.05.xml` — automatisch erzeugt am 2026-10-18 21:50 UTC
> 203 Stereotype mit Beziehungsregeln (Metaconstraints)

## Lesart

- **Erlaubte Ziele (client):** Der Stereotype darf nur als Quelle einer Beziehung zu den gelisteten Ziel-Stereotypen stehen.
- **Erlaubte Quellen (supplier):** Nur die gelisteten Stereotype dürfen als Ziel auf diesen Stereotype zeigen.
- **Weitere Rollen:** zusätzliche Metamodell-Beschränkungen (Rollennamen direkt aus der MDG).

| Stereotype | Erlaubte Ziele (client) | Erlaubte Quellen (supplier) | Weitere Rollen |
|---|---|---|---|
| AchievedEffect | Achiever | ActualState |  |
| ActivityPerformableUnderCondition | BusinessProcess | ActualCondition |  |
| ActivitySupportsService | OperationalActivity | ServiceSpecification |  |
| ActsUpon | OperationalActivityAction | PaperForm |  |
| ActualCondition |  |  | classifier → Condition |
| ActualConditionToActualResource | ActualResource | ActualCondition |  |
| ActualEnduringTask |  |  | classifier → EnduringTask |
| ActualEnterprisePhase |  |  | classifier → EnterprisePhase |
| ActualEnvironment |  |  | classifier → Environment |
| ActualLocation |  |  | classifier → Location |
| ActualMeasurement |  |  | definingFeature → Measurement, owningInstance → ActualPropertySet |
| ActualMeasurementSetAppliesFor | ActualMeasurementSet | MeasurableElement |  |
| ActualOrganization |  |  | classifier → Organization |
| ActualOrganizationRole |  |  | definingFeature → SubOrganization, owningInstance → ActualOrganization |
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
| ActualResourceRelationship |  |  | informationSource → ActualResource, informationTarget → ActualResource, realizes → ResourceExchange |
| ActualResourceRole |  |  | definingFeature → ResourceRole, owningInstance → ActualResource |
| ActualResourceToActualProjectMilestone | ActualResource | ActualProjectMilestone |  |
| ActualService |  |  | classifier → ServiceSpecification |
| ActualServiceSpecificationRole |  |  | definingFeature → ServiceSpecificationRole, owningInstance → ActualService |
| AffectedActivity | OperationalExchangeItem | OperationalActivity |  |
| AffectedFunctions | ResourceExchangeItem | Function |  |
| AffectedResource | OperationalActivity | OperationalExchangeItem |  |
| AlignsWithGoal | ServiceSpecification | EnterpriseGoal |  |
| ArbitraryConnector | ConceptRole | ConceptRole |  |
| ArchitecturalReference | ArchitecturalDescription | ArchitecturalDescription |  |
| ArchitecturalSequence | ArchitecturalDescription | ArchitecturalDescription |  |
| ArchitectureForProject | ActualProjectMilestone | ArchitecturalDescription |  |
| ArchitectureMetadata |  |  | annotatedElement → ArchitecturalDescription |
| BoundaryCondition | ResourceConnector | Environment |  |
| CapabilityDependency | Capability | Capability |  |
| CapabilityForTask | Capability | EnduringTask |  |
| CapabilityGeneralization |  |  | source → Capability, target → Capability |
| CapabilityRole |  |  | class → Capability, type → Capability |
| CapabilityRoleDependency | CapabilityRole | CapabilityRole |  |
| Checks | FitCriterion | BWRequirement |  |
| Classified | ServiceSpecification | Classification |  |
| Command |  |  | conveyed → DataElement, informationSource → ResourceRole, informationTarget → ResourceRole |
| CompetenceForRole | ResourceRole | Competence |  |
| CompliesViewpoint | View | Viewpoint |  |
| ConceptRole |  |  | class → HighLevelOperationalConcept, type → ConceptItem |
| ConcernForActualEnterprisePhase | ActualEnterprisePhase | Concern |  |
| ConcernForView | View | Concern |  |
| ConcernForViewpoint | Viewpoint | Concern |  |
| ConflictsWith | BWRequirement | BWRequirement |  |
| ConformsTo | UAFElement | Standard |  |
| ConsumedBy | ServiceSpecificationRole | OperationalRole |  |
| Consumes | OperationalActivityAction | ServiceSpecification |  |
| Control |  |  | conveyed → DataElement, informationSource → ResourceRole, informationTarget → ResourceRole |
| DataElement |  |  | owner → DataModel |
| DataElementStoredIn | DataElement | ResourceRole |  |
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
| FunctionControlFlow |  |  | source → FunctionAction;JoinNode;MergeNode, target → FunctionAction;JoinNode;MergeNode |
| FunctionEdge |  |  | owner → Function |
| FunctionObjectFlow |  |  | source → FunctionAction;JoinNode;MergeNode, target → FunctionAction;JoinNode;MergeNode |
| FunctionSubject | Function | ResourceExchangeItem |  |
| GoalForActualEnterprisePhase | ActualEnterprisePhase | EnterpriseGoal |  |
| HostedOn | ResourceRole | ResourceRole |  |
| Implements | StrategicConstraint | StrategicConstraint |  |
| ImplementsProtocol | ProtocolImplementation | Protocol |  |
| Information |  |  | annotatedElement → UAFElement |
| InformationElement |  |  | owner → DataModel |
| InformationRole |  |  | class → OperationalAsset, type → InformationElement |
| IsAccountableFor | Organization | ServiceSpecification |  |
| IsCapableToPerform | ServiceSpecification | ServiceFunctionAction |  |
| IsDuplicateOf | BWRequirement | BWRequirement |  |
| IsEquivalentToStandardElement | UAFElement | UAFElement |  |
| IsResponsibleFor | Organization | ServiceSpecification |  |
| JustifiedBy | StrategicConstraint | Reference |  |
| LocationType | LocationHolder | Location |  |
| MapsToCapability | BusinessProcess | Capability |  |
| Measurement |  |  | class → PropertySet, type → MeasurementType |
| Metadata |  |  | annotatedElement → UAFElement |
| MilestoneDependency | ActualProjectMilestone | ActualProjectMilestone |  |
| NeedsModificationOf | ActualProject | ResourceRole |  |
| NeedsResource | ActualProject | ResourceRole |  |
| NeedsService | ActualProject | ServiceSpecificationRole |  |
| OperationalActivity |  |  | ownedParameter → OperationalParameter |
| OperationalActivityAction |  |  | activity → OperationalActivity, behavior → OperationalActivity |
| OperationalActivityEdge |  |  | owner → OperationalActivity |
| OperationalAgent |  |  | ownedOperation → OperationalMethod, ownedPort → OperationalPort |
| OperationalArchitectureOfEnterprisePhase | ActualEnterprisePhase | OperationalArchitecture |  |
| OperationalConnector |  |  | end[0].role → OperationalRole, end[1].role → OperationalRole |
| OperationalControlFlow |  |  | source → OperationalActivityAction, target → OperationalActivityAction |
| OperationalExchange | OperationalActivity | OperationalActivity | conveyed → OperationalExchangeItem, informationSource → ServiceSpecification, informationTarget → ServiceSpecification, realizingActivityEdge → OperationalActivityEdge, realizingConnector → OperationalConnector, realizingMessage → OperationalMessage |
| OperationalMessage |  |  | receiveEvent.event.operation → OperationalMethod |
| OperationalMessageFlow |  |  | source → OperationalActivityAction, target → OperationalActivityAction |
| OperationalMethod |  |  | method → OperationalActivity, ownedOperation → OperationalInterface, ownedParameter → OperationalParameter |
| OperationalObjectFlow |  |  | source → OperationalActivityAction, target → OperationalActivityAction |
| OperationalParameter |  |  | type → OperationalExchangeItem |
| OperationalPort |  |  | class → OperationalAgent, type → OperationalInterface |
| OperationalRole |  |  | class → OperationalPerformer, type → OperationalPerformer |
| OperationalSignalProperty |  |  | class → OperationalSignal, type → OperationalExchangeItem |
| OperationalStateDescription |  |  | owner → OperationalAgent |
| OriginatesFrom | UAFElement | Reference |  |
| OwnedMilestone | ActualProject | ActualProjectMilestone |  |
| OwnsActualMeasurementSet | MeasurableElement | ActualMeasurementSet |  |
| OwnsMeasurement | MeasurableElement | MeasurementType |  |
| OwnsProcess | ActualOrganizationalResource | OperationalActivity |  |
| PartOfCatalogue |  |  | source → RequirementCategory, target → RequirementCatalogue |
| PartOfCategory |  |  | source → RequirementCategory, target → RequirementCategory |
| PerformsInContext | ServiceSpecificationRole | ServiceFunctionAction |  |
| PhysicalArchitectureOfEnterprisePhase | ActualEnterprisePhase | ResourceArchitecture |  |
| PhysicalLocation | LocationHolder | ActualLocation |  |
| PostRole |  |  | class → Post, type → Post |
| ProblemDomain |  |  | class → OperationalArchitecture, type → OperationalPerformer |
| ProcessGeneralization |  |  | source → BusinessProcess, target → BusinessProcess |
| ProjectMilestoneRole |  |  | class → Project, type → ProjectMilestone |
| ProjectMilestoneToProjectTheme | ProjectMilestone | ProjectTheme |  |
| ProjectProvidesFunction | ActualProject | Function |  |
| ProjectRole |  |  | class → Project, type → Project |
| ProjectSequence | ActualProject | ActualProject |  |
| ProjectStatus |  |  | definingFeature → ProjectTheme |
| ProjectSupportActivity | ActualProject | OperationalActivity |  |
| PropertySetGeneralization |  |  | source → System, target → System |
| ProtocolLayer |  |  | class → Protocolstack, type → Protocol |
| Provides | OperationalRole | ServiceSpecificationRole |  |
| ProvidesCompetence | ActualOrganizationalResource | Competence |  |
| ProvidesServiceFunction | ServiceInterface | ServiceFunction |  |
| RatifiedStandards | ActualOrganization | Standard |  |
| RealiseRequirement | Standard | BWRequirement |  |
| RealizedDesiredEffect | AchievedEffect | DesiredEffect |  |
| RealizesRecommendation | UAFElement | Recommendation |  |
| RealizingAchievedEffect | DesiredEffect | AchievedEffect |  |
| RefersTo | Recommendation | Finding |  |
| Refines | BWRequirement | BWRequirement |  |
| Replaces | BWRequirement | BWRequirement |  |
| ReplaceStandardElement | UAFElement | UAFElement |  |
| RequiredEnvironment | LocationHolder | ActualEnvironment |  |
| RequiredResource | ProjectMilestone | ResourcePerformer |  |
| Requires | BWRequirement | BWRequirement |  |
| RequiresCompetence | OrganizationalResource | Competence |  |
| ResourceConnector |  |  | end[0].role → ResourceRole, end[1].role → ResourceRole |
| ResourceDependency | ResourceRole | ResourceRole |  |
| ResourceExchange |  |  | conveyed → ResourceExchangeItem, informationSource → ServiceSpecificationRole, informationTarget → ServiceSpecificationRole, realizingActivityEdge → FunctionEdge, realizingConnector → ResourceConnector, realizingMessage → ResourceMessage |
| ResourceMessage |  |  | Connector → ResourceConnector, receiveEvent.event.operation → ResourceMethod |
| ResourceMethod |  |  | method → Function, ownedOperation → ResourcePerformer, ownedParameter → ResourceParameter |
| ResourceParameter |  |  | ownedParameter → Function, type → ResourceExchangeItem |
| ResourcePerformer |  |  | ownedPort → ResourcePort |
| ResourcePort |  |  | class → ResourcePerformer, type → ResourceInterface |
| ResourceRole |  |  | class → ResourcePerformer, type → ResourcePerformer |
| ResourceSignalProperty |  |  | class → ResourceSignal, type → ResourceExchangeItem |
| ResourceStateDescription |  |  | owner → ResourcePerformer |
| ResourceToServiceDependency | ResourceRole | ServiceSpecificationRole |  |
| Responsible | ActualProject | ServiceSpecification |  |
| ResultsFrom | Finding | UAFElement |  |
| SameAs | UAFElement | UAFElement |  |
| Satisfy | SubjectOfResourceConstraint | StrategicConstraint |  |
| SecurityConstraint |  |  | constrainedElement → SubjectOfSecurityConstraint |
| ServiceConnector |  |  | end[0].role → ServiceSpecificationRole, end[1].role → ServiceSpecificationRole |
| ServiceDependency | ServiceSpecification | ServiceSpecification |  |
| ServiceExchange |  |  | realizingConnector → ServiceConnector, realizingMessage → ServiceMessage, source → ServiceSpecification, target → ServiceSpecification |
| ServiceFunction |  |  | ownedParameter → ServiceParameter |
| ServiceFunctionAction |  |  | activity → ServiceFunction, behavior → ServiceFunction |
| ServiceGeneralization |  |  | source → ServiceSpecification, target → ServiceSpecification |
| ServiceInterface |  |  | ownedOperation → ServiceMethod |
| ServiceMethod |  |  | method → ServiceFunction, ownedParameter → ServiceParameter, receiveEvent.event.operation → ServiceMessage |
| ServiceParameter |  |  | type → OperationalExchangeItem |
| ServicePort |  |  | class → ServiceSpecification, type → ServiceInterface |
| ServiceProvision | ResourceRole | ServiceSpecificationRole |  |
| ServiceSpecification |  |  | ownedOperation → ServiceMethod, ownedPort → ServicePort |
| ServiceSpecificationRole |  |  | class → ServiceSpecification, type → ServiceSpecification |
| ServiceStateDescription |  |  | owner → ServiceSpecification |
| StakeholderConcern | Stakeholder | Concern |  |
| StatementTask | ActualEnterprisePhase | ActualEnduringTask |  |
| StemsFrom | BWRequirement | BWRequirement |  |
| SubOrganization |  |  | class → Organization, type → Organization |
| SuccessorOf | Standard | Standard |  |
| TemporalPart |  |  | class → EnterprisePhase, type → EnterprisePhase |
| ToBeRealizedBy | BWRequirement | Standard |  |
| VersionOfConfiguration |  |  | class → WholeLifeConfiguration, type → VersionedElement |
| VersionReleased | ActualProjectMilestone | VersionedElement |  |
| VersionSuccession | VersionOfConfiguration | VersionOfConfiguration |  |
| VersionWithdrawn | ActualProjectMilestone | VersionedElement |  |
| ViewpointsInArchitecturalDescription | ArchitecturalDescription | Viewpoint |  |
| ViewpointToStakeholder | Viewpoint | Stakeholder |  |
| ViewsInArchitecturalDescription | ArchitecturalDescription | View |  |
| VisionForActualEnterprisePhase | ActualEnterprisePhase | EnterpriseVision |  |