class CSVFile():

  def __init__(self, name):
    self.name = name

  def get_data(self):
    list = []
    
    my_file = open(self.name, 'r')

    for line in my_file:
      elements = line.split(',')
      if(elements[0] != 'Date'):
        elements[1] = elements[1].replace('\n','')
        list.append(elements)
        
      
    return list
      


    
    
    
  
  
  

 

      

  
    