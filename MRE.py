from pyhugin96 import *
from itertools import combinations, product 

net_name = "simplified_promedas"
promedas = Domain.parse_domain("{}.net".format(net_name))
promedas.open_log_file("{}.log".format(net_name))
promedas.triangulate()
promedas.compile()

disease_nodes = {
    'Flu', 
    'Stroke', 
    'Concussion', 
    'CommonCold', 
    'PeanutAllergy', 
    'Depression', 
    'Pneunomia', 
    'Hypertension', 
    'Asthma'
}

# Some possible evidence
evidence = [
    { "Coughing":1 },
    {"Coughing":1, "Diarrhea":1,"HeadAche" :1,"Tired":1,"LossSmell":0},
    {"AtePeanut" :0, "Coughing":1, "Diarrhea":1, "Naussea":1 },
    {"AtePeanut" :1, "Coughing":1, "Diarrhea":1, "Naussea":1 },
    {"HeadAche" :1, "BadMood":1, "MemoryIssues":1},
    {"HeadAche" :0, "BadMood":1, "MemoryIssues":1},
    { "BadMood":1, "MemoryIssues":1},
    {"HeadAche" :0, "BadMood":1, "MemoryIssues":1,"Naussea":1 },
    {"HeadAche" :1, "BadMood":1, "MemoryIssues":1,"Naussea":1 },
    {"TroubleSpeaking" :1},
    {"TroubleSpeaking" :0},
    { "TroubleSpeaking" : 1 , "Dizziness" : 1},
    { "TroubleSpeaking" : 1 , "Dizziness" : 0} ,
    {"TroubleSpeaking" : 0 , "Dizziness" : 1},
    { "TroubleSpeaking" : 0 , "Dizziness" : 1, "visionProblems" : 1},
    { "TroubleSpeaking" : 1 , "Dizziness" : 1, "visionProblems" : 1},
    { "TroubleSpeaking" : 1 , "Dizziness" : 1, "visionProblems" : 0},
    { "TroubleSpeaking" : 0 , "Dizziness" : 1, "visionProblems" : 1, "Coughing" : 1, "Diarrhea" : 1},
    { "TroubleSpeaking" : 1 , "Dizziness" : 1, "visionProblems" : 1, "Coughing" : 1, "Diarrhea" : 1},
    { "Dizziness" : 1, "visionProblems" : 1, "Coughing" : 1, "Diarrhea" : 1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1 },
    {"Tired":0, "Coughing":1, "Diarrhea":1, "Naussea":1 },
    {"Tired":1, "Coughing":1, "Diarrhea":1 },
    {"Naussea":1, "Coughing":1, "Diarrhea":1 },
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1 ,"AtePeanut":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1 ,"AtePeanut":0},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "AtePeanut":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "AtePeanut":0},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "TroubleSpeaking":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "TroubleSpeaking":1, "AtePeanut":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "TroubleSpeaking":1, "AtePeanut":0},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "HeadAche":1, "visionProblems":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "HeadAche":1, "visionProblems":1, "MemoryIssues":1},
    {"Tired":1, "Coughing":1, "Diarrhea":1, "Naussea":1, "LossSmell":1, "BadMood":1},
    {"HeadAche" :1},
    {"HeadAche" :0},
    {"HeadAche" :1, "AbnormTemp":1},
    {"HeadAche" :1, "AbnormTemp":0, "MuscleAche":1},
    {"HeadAche" :1, "AbnormTemp":1, "MuscleAche":1},
    {"HeadAche" :0, "AbnormTemp":1, "MuscleAche":1},
    {"HeadAche" :1, "AbnormTemp":0, "MuscleAche":1, "Coughing":1, "Diarrhea":1},
    {"HeadAche": 0,"visionProblems":1, "MemoryIssues":1},
    {"HeadAche": 1,"visionProblems":1, "MemoryIssues":1},
    {"HeadAche": 1,"MuscleAche":1, "AbnormTemp":1,"Naussea":1,"Diarrhea":1, "Coughing":1},
    {"HeadAche": 1,"MuscleAche":1, "AbnormTemp":0,"Naussea":1,"Diarrhea":0, "Coughing":1},
    {"ShortnessBreath":1, "ThigthChest": 1},
    {"ShortnessBreath":1, "ThigthChest": 1, "AbnormTemp":1},
    {"ShortnessBreath":1, "ThigthChest": 1, "AbnormTemp":1, 'Coughing':1},
    {"ThigthChest": 1, "AbnormTemp":1, 'Coughing':1},
    {"ShortnessBreath":1, "ThigthChest": 1, "AbnormTemp":1, 'Coughing':0},
    {"Tired":1,"LossSmell":1,"Coughing":1,"AtePeanut":1},
    {"Tired":1,"LossSmell":1,"Coughing":1,"ThigthChest":1},
    {"Tired":0,"LossSmell":1,"Coughing":1,"ThigthChest":1},
    {"MuscleAche":1,"AbnormTemp":1,"Dizziness":1,"Diarrhea":1,"Naussea":1},
    {"MuscleAche":1,"AbnormTemp":1,"Dizziness":0,"Diarrhea":1,"Naussea":1},
    {"MuscleAche":1,"AbnormTemp":1,"Dizziness":0,"Diarrhea":0,"Naussea":1},
    {"AbnormTemp":1,"Diarrhea":0,"Dizziness":0,"MuscleAche":1,"Naussea":0},
    {"MuscleAche":1,"AbnormTemp":0,"Dizziness":0,"Diarrhea":0,"Naussea":0},
    {"BadMood":1, "Tired":1},
    {"BadMood":1, "Tired":1, "MemoryIssues":1},
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":1} ,
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":1, "BadMood":1},
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":1, "BadMood":0},
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":1, "Diarrhea":1},
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":1, "Diarrhea":1, "Naussea":1},
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":1, "Diarrhea":1, "Naussea":0},
    {"AtePeanut":1, "HeadAche":1, "MemoryIssues":0},
    {"LossSmell":1,"Tired":1,"AbnormTemp":1,"Diarrhea":1},
    {"LossSmell":1,"Tired":1,"ShortnessBreath":1,"AbnormTemp":1,"Diarrhea":1},
    {"LossSmell":1,"Tired":1,"ShortnessBreath":1,"AbnormTemp":1,"Diarrhea":0},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"Dizziness":1,"Naussea":1},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"Dizziness":0,"Naussea":0},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"Dizziness":0,"Naussea":1},
    {},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"LossSmell":1,"Naussea":1, "MemoryIssues":1,"MuscleAche":1, "ThigthChest":1, "HeadAche":1,"TroubleSpeaking":1,"Dizziness":1,"visionProblems":1,"BadMood":1,"Diarrhea":1,"AtePeanut":1,"AbnormTemp":1},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"LossSmell":1,"Naussea":1, "MemoryIssues":1,"MuscleAche":1, "ThigthChest":1, "HeadAche":1,"BadMood":1,"Diarrhea":1,"AtePeanut":1,"AbnormTemp":1},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"LossSmell":1,"Naussea":1, "MemoryIssues":1,"MuscleAche":1, "ThigthChest":1, "HeadAche":1,"BadMood":1,"Diarrhea":1,"AtePeanut":1,"AbnormTemp":1, "Dizziness":1, "visionProblems":1},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"LossSmell":1,"Naussea":1,"MuscleAche":1, "ThigthChest":1, "HeadAche":1,"BadMood":1,"Diarrhea":1,"AtePeanut":1,"AbnormTemp":1},
    {"Coughing":1, "ShortnessBreath":1,"Tired":1,"LossSmell":1,"Naussea":1,"MuscleAche":1, "ThigthChest":1, "BadMood":1,"Diarrhea":1,"AtePeanut":1,"AbnormTemp":1},
    {"visionProblems":1},
    {"visionProblems":1,"Tired":1,"BadMood":1},
    {"visionProblems":1,"Tired":1,"MemoryIssues":1},
    {"Tired":1},
    {"Tired":1,"BadMood":1},
    {"AbnormTemp":1},
    {"AbnormTemp":1, "Coughing":0, "ThigthChest":1,"ShortnessBreath":1},
    {"AbnormTemp":1, "Coughing":0, "ThigthChest":1,"ShortnessBreath":1, "Naussea":0},
    {"Coughing":1,"LossSmell":1,"Tired":1},
    {"Coughing":1,"LossSmell":1,"Tired":1,"HeadAche":0,"ThigthChest":0,"visionProblems":0,"TroubleSpeaking":0,"Naussea":0,"MemoryIssues":0,"Dizziness":0,"Diarrhea":0,"BadMood":0,"AbnormTemp":0},
    {"AtePeanut":1,"LossSmell":0,"Naussea":0,"Diarrhea":1,"Coughing":1},
    {"Coughing":1,"MemoryIssues":1,"HeadAche":1,"visionProblems":1,"ShortnessBreath":1},
    {"Coughing":1,"MemoryIssues":1,"HeadAche":1,"visionProblems":1,"ShortnessBreath":1,"ThigthChest":0},
    {"Coughing":1,"MemoryIssues":1,"HeadAche":1,"visionProblems":1,"ShortnessBreath":1,"ThigthChest":1},
    {"Naussea":1,"MemoryIssues":1,"HeadAche":1,"visionProblems":1,"Dizziness":1,"AbnormTemp":1},
    {"AbnormTemp":1,"HeadAche":1,"Naussea":0},
    {"AbnormTemp":1,"HeadAche":1,"Naussea":0,"Coughing":0},
    {"AbnormTemp":0,"HeadAche":1,"Naussea":0,"Coughing":0,"MuscleAche":0,"Diarrhea":0}]

def reset(domain):
    if not domain.is_compiled():
        domain.compile()
    domain.retract_findings()
    domain.propagate()

def set_evidence(evidence):
    if evidence:
        for node_name, state in evidence.items():
            node = promedas.get_node_by_name(node_name)
            node.select_state(state)

def prob_E(evidence):
    """
    Computes P(Evidence) for the given evidence.
    P(Evidence) is equal to the sum of the probabilties of the evidence occuring given all possible
    configurations of the variable it depends on.
    The probaility of E given a certain configuration is equal to the product of the likelhood of the evidence
    given a configuration and the probality of that configuration

    Args:
        evidence (dict): A dictionary of evidence variables and their states.
    
    Returns:
        totalSum (float): The probability of the evidence.
    """

    # Get the nodes on which the evidence variables depends on
    nodesIn=[]
    for node_name, state in evidence.items():
        evi = promedas.get_node_by_name(node_name)
        evi.generate_table()
        nodes = evi.get_table().get_nodes()
        for node in nodes:
            if node.get_name() in disease_nodes and node.get_name() not in nodesIn:
                nodesIn.append(node.get_name()) 
        
    # Make a list of dicts containing all possible combinations of the nodes, wheter the dissease is present or not
    combinations = list(product([0, 1], repeat=len(nodesIn)))
    configs = [dict(zip(nodesIn, values)) for values in combinations]
    
    # Compute the probability of the evidence by iterating over all configurations (marginalization)
    totalSum = 0
    for config in configs:
            intermediateVal = 1

            # Compute the probability of the configuration.
            for node_name, state in config.items():
                node = promedas.get_node_by_name(node_name)
                p = node.get_table().get_data()[state]
                intermediateVal= intermediateVal* p

            # Compute the probability of the evidence given the configuration.
            for node_name, state in evidence.items():
                evi = promedas.get_node_by_name(node_name)
                evi.generate_table()
                nodes = evi.get_table().get_nodes()

                # Compute the index of the probality table for the evidence given the configuration to retrieve the correct probability.
                values = ''
                for node in nodes:
                    if node.get_name() not in disease_nodes:
                        values = values+ str(state)
                    else:
                        values = values+ str(config[node.get_name()])

                index = int(values, 2)
                p = evi.get_table().get_data()[index]
                intermediateVal= intermediateVal* p

            totalSum = totalSum + intermediateVal
    return totalSum        

 
def computeProbConfigMRE(config, evidence,pe ): 
    """
    Compute the probability of the disease config given the evidence.
    P(X|E)

    Args:
        evidence (dict): A dictionary of evidence variables and their states.
        config (dict): A dictionary of disease variables and their states.
        pe (float): Probability of the evidence p(E).
    
    Returns:
        (float): The probability of the disease configuration given the evidence.
    """
    
    # Compute p(X)
    probabilityX = 1
    for node_name, state in config.items():
        evi = promedas.get_node_by_name(node_name)   
        probabilityX= probabilityX* evi.get_table().get_data()[state]
 
    # Get diseases not in the configuration and get all possible configurations thereof
    fixed = {d: 1 for d in config}
    unknown = [d for d in disease_nodes if d not in config]
    combinations = list(product([0, 1], repeat=len(unknown)))

    # Make list of full configurations
    states = []
    for combo in combinations:
        state = fixed.copy()
        for d, v in zip(unknown, combo):
            state[d] = v
        states.append(state)

    # perform marganilization to compute P(E|x)
    sumHidden = 0
    for full_config  in states:

        # Compute p(X_unkown)
        pxHidden = 1
        for node_name, state in full_config.items():
            if(node_name not in config):
                evi = promedas.get_node_by_name(node_name)   
                pxHidden= pxHidden* evi.get_table().get_data()[state]


        # Compute P(E|x,xhidden) 
        p =1
        for node_name, state in evidence.items():

            evi = promedas.get_node_by_name(node_name)
            evi.generate_table()
            nodes = evi.get_table().get_nodes()
            values = ''
            hiddeNodes = []
            for node in nodes:
                if node.get_name() not in disease_nodes:
                    hiddeNodes.append('')
                    values = values+ str(state)
                elif node.get_name() in full_config and node.get_name() in disease_nodes:
                    values = values+ str(full_config[node.get_name()])
                    hiddeNodes.append('')
            index = int(values, 2)
            p =p* evi.get_table().get_data()[index]
        
        # Marginalize
        sumHidden = sumHidden +p*pxHidden

    return (sumHidden*probabilityX)/pe

def computeGBF(pConfig, config):
    """
    Compute the GBF (generalized bayes factor) for a given instantiation of the target variables.
    GBF = P(x|evidence)*(1-P(x))/(P(x)*(1-P(x|Evidence))). GBF measures the incresed liklihood 
    of the instantiation by comparing the postior and prior probabilities.

    Args:
        config (dict): A dictionary containing the target variables and their states.
        pConfig (float): the valua that is equal to P(X|evidence).

    Returns:
        GBF (float): The gbf corresponding the configuration and evidence.
       
    """

    # Compute P(X)).
    prob = 1
    for node_name, state in config.items():
        node = promedas.get_node_by_name(node_name)
        p = node.get_table().get_data()[state]
        prob= prob* p
        
    # GBF = P(x|evidence)*(1-P(x))/(P(x)*(1-P(x|Evidence)))
    GBF = (pConfig*(1-prob))/(prob*(1-pConfig))

    return GBF

def MRE(evidence,ExplainationSet):
    """
    Compute the top 5 MRE explanations for the given evidence. Where MRE is equal
    to maximized GBF where we maximize over the configuration. Hence computing the
    configuration with mist increase in liklihood compared to the prior belief.

    Args:
        evidence (dict): A dictionary of evidence variables and their states.
        ExplainationSet (List): A list of all target nodes.
        
    
    Returns:
        top5Config (list): A list of the top 5 MRE configurations.
        top5GBF (list): A list of the GBF values corresponding to the top 5 configurations.
    """

    # Create a list of all possible configurations.
    promedas.retract_findings()
    set_evidence(evidence)
    promedas.propagate()
    nodeNames=[]   
    for dissease in ExplainationSet:
        node = dissease.get_name()
        nodeNames.append(node)  
    configs = [list(combinations(nodeNames, r)) for r in range(1, len(nodeNames) + 1)]  
    configs = [list(sublist) for g in configs for sublist in g]  

    # Store and compute the top 5 MRE explanations.
    top5GBF =  [0]*5
    top5Config = [()]*5

    # Compute the probabilityof the evidence
    pe = prob_E(evidence)

    for config in configs:

        diseaseDict ={disease: 1 for disease in config}

        # Compute P(X|Evidence) for the given configuration.
        configProb =  computeProbConfigMRE(diseaseDict,evidence,pe)
        
        # Compute the generalised bayesfactor for the given configuration given the evidence
        GBF=  computeGBF(configProb,diseaseDict)

        # Store and manage the top 5 MRE explanations.
        if GBF >=1:
            if len(top5GBF) < 5:
                top5GBF.append(GBF)
                top5Config.append(config)
            else:
                # Find the smallest value among the top 5
                min_value = min(top5GBF)
                min_index = top5GBF.index(min_value)

                # If the new value is bigger, replace the smallest one
                if GBF > min_value:
                    top5GBF[min_index] = GBF
                    top5Config[min_index] = config

    combined = list(zip(top5GBF, top5Config))
    combined.sort(key=lambda x: x[0], reverse=True)
    top5GBF[:], top5Config[:] = zip(*combined)
    return top5Config,top5GBF
      

evi = evidence[0]

# Create a list of nodes in the target set
ExplainationSet = [node for node in promedas.get_nodes() if node.get_name() in disease_nodes ]

topConfig, topGBF= MRE(evi,ExplainationSet)
for i in range(len(topConfig)):
        print("explanation # ",i+1,": ", topConfig[i])
        print("GBF: ",topGBF[i] ) 
