# Reads the itcont-formatted input and reorganizes it top_drug_cost-formatted output.
def pharmwrite(inputname, outputname):

    # Open input as a list
    inputfile = open(inputname).readlines()

    # Split list string
    data = [i.split(',') for i in inputfile]

    # Remove 'new line' for ease of identification
    for i in range(data.__len__()):
        for j in range(data[i].__len__()):
            data[i][j] = data[i][j].replace("\n", "")

    # Create index for drug_name and drug_cost columns of input data
    didx = data[0].index('drug_name')
    cidx = data[0].index('drug_cost')

    # Find the drugs and drug cost for each prescriber and put in separate list
    drugs = [None] * data.__len__()
    cost = [None] * data.__len__()
    for i in range(1, data.__len__()):
        drugs[i] = data[i][didx]
        cost[i] = data[i][cidx]
    drugs = drugs[1:drugs.__len__()]
    cost = cost[1:cost.__len__()]

    # Create set of all unique drugs (not the drug for each prescriber)
    uniq_drugs = set(drugs)

    # Get num_prescriber and total_cost
    num_prescriber = [None] * uniq_drugs.__len__()
    total_cost = [0] * uniq_drugs.__len__()
    idx = 0  # Used for indexing in the loop
    for i in uniq_drugs:
        # Get count of prescribers for drug i
        num_prescriber[idx] = drugs.count(i)
        # Create index for drugs for uniq_drugs[i]
        indices = [k for k, x in enumerate(drugs) if x == i]
        # Loop through cost of each drug[indices] for uniq_drugs[i]
        for j in indices:
            total_cost[idx] = int(total_cost[idx]) + int(cost[j])
        idx = idx + 1

    # Clean and format output
    output_data0 = str('drug_name, num_prescriber, total_cost')
    output_data1 = str(uniq_drugs)
    output_data2 = str(num_prescriber)
    output_data3 = str(total_cost)

    # Remove listforms (stuff that got left behind from converting from list to string)
    listforms = ["{", "}", "'", "[", "]"]  # Formatting from list to string that needs to be removed
    for i in listforms:
        output_data0 = output_data0.replace(i, "")
        output_data1 = output_data1.replace(i, "")
        output_data2 = output_data2.replace(i, "")
        output_data3 = output_data3.replace(i, "")

    output_data = [output_data0, output_data1, output_data2, output_data3]

    # Open output for writing
    outputfile = open(outputname, 'w+')

    # Write output
    for line in output_data:
        outputfile.write("%s\n" % line)

    # Close opened output file
    outputfile.close()
