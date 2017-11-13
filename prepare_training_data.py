import codecs
import zipfile

from lxml import etree
import json
from lib.unicodeConvert import *
import glob

def get_word_xml(docx_filename):
   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

def get_xml_tree(xml_string):
   return etree.fromstring(xml_string)


def itertext(my_etree):
    """Iterator to go through xml tree's text nodes"""
    doc = []
    for node in my_etree.iter(tag=etree.Element):
        if _check_element_is(node, 'p'):
            print_node(node=node, doc=doc)

    return doc

def print_node(node, doc):
    p = []
    for e in node.iter(tag=etree.Element):
        if _check_element_is(e, 't'):
            if e.text is not None:
                if e.text.strip() != '':
                    p.append(e.text)

    if len(p) > 0:
        doc.append(' '.join(p))

def _check_element_is(element, type_char):
    word_schema = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    return element.tag == '{%s}%s' % (word_schema, type_char)

def write_file(file_name, data):
    with codecs.open(file_name, "w", encoding="utf-8") as f:
        f.write(data)
    f.close()

def check_section_exits(section, sections):
    for s in sections:
        if section.lower().find("section") > -1 and section.lower().find(s.lower()) > -1:
            return True
    return False

def check_subsection_exits(section, sections):
    sec = ''.join([index for index in section if not index.isdigit() and index != '.' and index != ':'])
    for s in sections:
        sec = sec.replace('(expected or ex-post)', '')
        if sec.strip().lower() == s.lower():
            return True
    return False

def update_data(doc, data):
    sections = []
    for section in data["meta"]["section_names"]:
        sections.append(section)
    for section in data["meta"]["section_names"]:
        sec_data = extract_section(doc, section, sections)
        for subsection in data["meta"]["section_names"][section]:
            subsec_data = extract_subsection(sec_data, subsection, data["meta"]["section_names"][section])
            if len(data["meta"]["section_names"][section][subsection]) > 0:
                for subsubsection in data["meta"]["section_names"][section][subsection]:
                    subsubsec_data = extract_subsubsection(subsec_data, subsubsection, data["meta"]["section_names"][section][subsection])
                    if len(subsubsec_data) > 0:
                        if len(data["meta"]["section_names"][section][subsection][subsubsection]) > 0:
                            for subsubsubsection in data["meta"]["section_names"][section][subsection][subsubsection]:
                                subsubsubsec_data = extract_subsubsection(subsubsec_data, subsubsubsection,
                                                                    data["meta"]["section_names"][section][subsection][subsubsection])
                                if len(subsubsubsec_data) > 0:
                                    fill_3_level_data(subsubsubsec_data, section, subsection, subsubsection, subsubsubsection, data)

                            # clear the content of 3-level data
                            new_subsubsec_data = []
                            for x in range(0, len(subsubsec_data)):
                                if check_subsection_exits(subsubsec_data[x],
                                                          data["meta"]["section_names"][section][subsection][subsubsection]):
                                    break
                                new_subsubsec_data.append(subsubsec_data[x])
                            subsubsec_data = new_subsubsec_data
                        fill_2_level_data(subsubsec_data, section, subsection, subsubsection, data)

                # clear the content of 1-level data
                new_subsec_data = []
                for x in range(0, len(subsec_data)):
                    if check_subsection_exits(subsec_data[x], data["meta"]["section_names"][section][subsection]):
                        break
                    new_subsec_data.append(subsec_data[x])
                subsec_data = new_subsec_data

            fill_level_data(subsec_data, section, subsection, data)
    return data

def check_checkbox_exists(line):
    s = line.split(' ')
    decimal_w = ''
    for w in s:
        try:
            decimal_w = python_to_ncr(w, decimal=True)
        except:
            pass

        if decimal_w == '&#9746;'or decimal_w == "&#9744;":
            return True
    return False

def fill_2_level_data(subsec_data, section, subsection, subsubsection, data):
    for line in subsec_data:
       if check_checkbox_exists(line):
            s = line.split(' ')
            ss = []
            for i, w in enumerate(s):
                decimal_w =''
                ss.append(w)
                try:
                    decimal_w = python_to_ncr(s[i + 1], decimal=True)
                except:
                    pass
                if decimal_w == '&#9746;' or decimal_w == "&#9744;" or (i + 1) == len(s):
                    checked = False
                    try:
                        decimal_w = python_to_ncr(ss[0], decimal=True)
                    except:
                        pass
                    if decimal_w == '&#9746;':
                        checked = True
                    ss.remove(ss[0])
                    if ' '.join(ss).lower().find("other (please specify):") > -1:
                        ws = "other (please specify):"
                        if len(' '.join(ss).lower()) > len(ws):
                            checked = True
                    data["form_data"]["sections"][section][subsection][subsubsection][' '.join(ss).lower()] = checked
                    ss = []

def fill_3_level_data(subsec_data, section, subsection, subsubsection,subsubsubsection, data):
    for line in subsec_data:
       if check_checkbox_exists(line):
            s = line.split(' ')
            ss = []
            for i, w in enumerate(s):
                decimal_w =''
                ss.append(w)
                try:
                    decimal_w = python_to_ncr(s[i + 1], decimal=True)
                except:
                    pass
                if decimal_w == '&#9746;' or decimal_w == "&#9744;" or (i + 1) == len(s):
                    checked = False
                    try:
                        decimal_w = python_to_ncr(ss[0], decimal=True)
                    except:
                        pass
                    if decimal_w == '&#9746;':
                        checked = True
                    ss.remove(ss[0])
                    if ' '.join(ss).lower().find("other (please specify):") > -1:
                        ws = "other (please specify):"
                        if len(' '.join(ss).lower()) > len(ws):
                            checked = True
                    data["form_data"]["sections"][section][subsection][subsubsection][subsubsubsection][' '.join(ss).lower()] = checked
                    ss = []


def fill_level_data(subsec_data, section, subsection, data):
    for line in subsec_data:
       if check_checkbox_exists(line):
            s = line.split(' ')
            ss = []

            for i, w in enumerate(s):
                decimal_w =''
                ss.append(w)
                try:
                    decimal_w = python_to_ncr(s[i + 1], decimal=True)
                except:
                    pass
                if decimal_w == '&#9746;' or decimal_w == "&#9744;" or (i + 1) == len(s):
                    checked = False
                    try:
                        decimal_w = python_to_ncr(ss[0], decimal=True)
                    except:
                        pass
                    if decimal_w == '&#9746;':
                        checked = True
                    ss.remove(ss[0])
                    if ' '.join(ss).lower().find("other (please specify):") > -1:
                        ws = "other (please specify):"
                        if len(' '.join(ss).lower()) > len(ws):
                            checked = True

                    data["form_data"]["sections"][section][subsection][' '.join(ss).lower()] = checked
                    ss = []

def extract_subsubsection(sec_data, subsection, subsections):
    start = -1
    subsec_data = []
    subsection = subsection.replace('(expected or ex-post)','')
    for i, line in enumerate(sec_data):
        s = ''.join([index for index in line if not index.isdigit() and index != '.' and index != ':'])
        s = s.replace('(expected or ex-post)', '')
        if s.strip().lower() == subsection.lower():
            start = i
            break
    if start >= 0:
        for x in range(start + 1, len(sec_data)):
            if check_subsection_exits(sec_data[x], subsections):
                break
            subsec_data.append(sec_data[x])
    return subsec_data

def extract_subsection(sec_data, subsection, subsections):
    start = -1
    subsec_data = []
    subsection = subsection.replace('(expected or ex-post)','')
    for i, line in enumerate(sec_data):
        if not line.islower():
            s = ''.join([index for index in line if not index.isdigit() and index != '.' and index != ':'])
            s = s.replace('(expected or ex-post)', '')
            if s.strip().lower() == subsection.lower():
                start = i
                break
        continue
    if start >= 0:
        for x in range(start + 1, len(sec_data)):
            if not sec_data[x].islower():
                if check_subsection_exits(sec_data[x], subsections):
                    break
            subsec_data.append(sec_data[x])
    return subsec_data

def extract_section(doc, section, sections):
    start = 0
    sec_data = []
    for i, line in enumerate(doc):
        if line.lower().find("section") > -1 and line.lower().find(section.lower()) > -1:
            start = i
            break
    for x in range(start + 1, len(doc)):
        if check_section_exits(doc[x], sections):
            break
        sec_data.append(doc[x])
    return sec_data

if __name__ == '__main__':
    green_and_social_bond_projects_files =  glob.glob("./data/raw_data/GREEN_AND_SOCIAL_BOND_PROJECTS_DOCX/*.docx")
    sustainalutics_files = glob.glob("./data/raw_data/SUSTAINALUTICS_DOCX/*.docx")
    for file in green_and_social_bond_projects_files:
        filename = file.split('/')[4]
        name = filename.split('.')[0]
        with open('./template/form_structure.json') as data_file:
            data = json.load(data_file)
        try:
            xml_content = get_word_xml(file)
            xml_tree = get_xml_tree(xml_content)
            tree = etree.tostring(xml_tree, pretty_print=True).decode()
            doc = itertext(xml_tree)
            data = update_data(doc, data)
            with open('./data/raw_data/FORMS/' + name +'.json', 'w') as outfile:
                outfile.write(json.dumps(data, sort_keys=True, indent = 4, separators = (',', ': ')))
            print filename + ' Done!'
        except:
            print filename + ' Fail!'
            pass

    for file in sustainalutics_files:
        filename = file.split('/')[4]
        name = filename.split('.')[0]
        with open('./template/form_structure.json') as data_file:
            data = json.load(data_file)
        try:
            xml_content = get_word_xml(file)
            xml_tree = get_xml_tree(xml_content)
            tree = etree.tostring(xml_tree, pretty_print=True).decode()
            doc = itertext(xml_tree)
            data = update_data(doc, data)
            with open('./data/raw_data/FORMS/' + name + '.json', 'w') as outfile:
                outfile.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
            print filename + ' Done!'
        except:
            print filename + ' Fail!'
            pass

    # try:
    #     with open('./template/form_structure.json') as data_file:
    #         data = json.load(data_file)
    #     xml_content = get_word_xml("./data/raw_data/Social-Bond-Second-Party-Opinion_NWB_erf.docx")
    #     xml_tree = get_xml_tree(xml_content)
    #     tree = etree.tostring(xml_tree, pretty_print=True).decode()
    #     doc = itertext(xml_tree)
    #     data = update_data(doc, data)
    #     print "done"
    # except:
    #     pass