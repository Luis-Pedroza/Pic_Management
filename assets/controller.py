from PIL import Image
import cv2
import os

class ReName():
    def New_Name(self, folder, name):
        counter = 1
        for file in os.listdir(folder):
            # Get extension 
            extension = os.path.splitext(file)[1]
            # New name
            newName = name + '_' + str(counter) + extension
            # routes of images
            original = os.path.join(folder, file)
            newFile = os.path.join(folder, newName)
            # re name the file
            os.rename(original, newFile)
            counter += 1

    def Delete_Name(self, folder, word_to_remove):
        counter = 1
        for file in os.listdir(folder):
            # Get name and extension
            file_name, extension = os.path.splitext(file)

            # Check if the word_to_remove is present in the file name
            if word_to_remove in file_name:
                # Remove the word_to_remove from the file name
                new_name = file_name.replace(word_to_remove, "")
                new_name = new_name.strip('_')  # Remove leading underscores if any
                
                # Update the file path
                original = os.path.join(folder, file)
                new_file = os.path.join(folder, new_name + extension)
                
                # Rename the file
                os.rename(original, new_file)
                counter += 1

class convert():
    def convert(self, folder, current, new):
        counter = 0

        # Lista de archivos en la carpeta
        files = os.listdir(folder)
        # Recorremos la lista de archivos
        for file in files:
            # Si la extensión es "webp"
            if current == "Todo" or current == "All" or file.endswith(f'.{current}'):
                counter += 1
                # Abrimos la imagen con Pillow
                image = Image.open(os.path.join(folder, file))
                # Creamos el nuevo nombre de archivo con extensión "png"
                
                newName = os.path.splitext(file)[0] + f'.{new}'
                # Guardamos la imagen en formato "png"
                image.save(os.path.join(folder, newName), new)
                # Cerramos la imagen
                image.close()
                if newName != file:
                # Eliminamos el archivo original
                    os.remove(os.path.join(folder, file))
class enhance():
    def enhance(self, folder):
        files = os.listdir(folder)
        
        for file in files:
            image = cv2.imread(f'{folder}/{file}')
            
            # Superresolución
            l, m, n = image.shape
            superresized_image = cv2.resize(image, (m*2, l*2))
            
            # Reducción de ruido
            denoised_image = cv2.fastNlMeansDenoisingColored(superresized_image, None, 10, 10, 7, 21)
            
            # Mejora de detalles y texturas
            enhanced_image = cv2.detailEnhance(denoised_image, sigma_s=10, sigma_r=0.10)
            
            # Ajuste de los colores mediante un mapeo lineal
            adjusted_image = cv2.normalize(enhanced_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            # Guardar la imagen mejorada
            cv2.imwrite(f'{folder}/Enhanced_{file}', adjusted_image)

