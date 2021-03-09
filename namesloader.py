# namesloader.py
# author: Christoph Waffler
class NamesLoader:
    def load_file(self, path_to_file: str, verbose=False):      
        with open(path_to_file) as f:
            content = f.readlines()
            
        content = [x.strip() for x in content]
        
        names_to_tag = dict()
        tag_to_names = dict()
        real_names = []
        discord_tags = []
        for i in range(len(content)):
            if i % 3 == 0:
                real_names.extend(content[i].split(", "))
                for i in range(len(real_names)):
                    real_names[i] = real_names[i].lower()
            elif i % 3 == 1:
                discord_tags.extend(content[i].split(", "))
            
            elif i % 3 == 2:
                for name in real_names:
                    names_to_tag[name] = discord_tags.copy()
                    
                for tag in discord_tags:
                    tag_to_names[tag] = real_names.copy()
                    
                    
                real_names.clear()
                discord_tags.clear()
                
        if (verbose == True):
            for name in names_to_tag:
                print(f"{name} -> {names_to_tag[name]}")
                
            for tag in tag_to_names:
                print(f"{tag} -> {tag_to_names[tag]}")
        
        return names_to_tag, tag_to_names