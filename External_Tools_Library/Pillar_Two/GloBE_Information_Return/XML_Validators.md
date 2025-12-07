# XML Validators for GIR Practice

Free tools for validating GIR XML files against the OECD schema.

## Online XML Validators

| Tool | URL | Features | Limitations |
|------|-----|----------|-------------|
| **FreeFormatter XML Validator** | https://www.freeformatter.com/xml-validator-xsd.html | Paste XML and XSD, instant validation | No file upload for large files |
| **XMLValidation.com** | https://www.xmlvalidation.com/ | Simple interface, supports file upload | Basic error messages |
| **Code Beautify XML Validator** | https://codebeautify.org/xmlvalidator | Validate against XSD, format XML | Ads on page |

## Desktop Tools (Free Versions)

| Tool | URL | Features | Limitations |
|------|-----|----------|-------------|
| **Notepad++ with XML Tools** | https://notepad-plus-plus.org/ | Free, lightweight, XML plugin available | Windows only |
| **VS Code with XML Extension** | https://code.visualstudio.com/ | Free, cross-platform, good XSD support | Requires extension setup |
| **XMLSpy (Trial)** | https://www.altova.com/xmlspy-xml-editor | Professional features, 30-day trial | Trial expires |

## How to Validate GIR XML

### Step 1: Get the OECD Schema
Download the official XSD from OECD (see OECD_Official_Resources.md)

### Step 2: Prepare Your XML
Export or create your GIR XML file

### Step 3: Validate
1. Open your chosen validator
2. Load the OECD XSD schema
3. Load your GIR XML
4. Run validation
5. Review and fix any errors

## Common Validation Errors

| Error Type | Cause | Solution |
|------------|-------|----------|
| **Missing required element** | Mandatory field not populated | Add the required element |
| **Invalid enumeration** | Code value not in allowed list | Use valid code from schema |
| **Type mismatch** | Wrong data type (text vs number) | Correct the data type |
| **Namespace error** | Wrong or missing namespace | Verify namespace declarations |

## Practice Tips

1. Start with a known-good sample XML from OECD
2. Make intentional errors to see validation messages
3. Practice fixing common errors before real filings

## Caution

- These free tools are for **learning and practice only**
- For actual filings, use professional-grade validation tools
- Always verify with jurisdiction-specific validators where available
