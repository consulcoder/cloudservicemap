<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output
            method="html"
            encoding="UTF-8"
            doctype-public="-//W3C//DTD HTML 4.01//EN"
            doctype-system="http://www.w3.org/TR/html4/strict.dtd"
            indent="yes"
    />

    <!-- template -->
    <xsl:template match="/">
        <html>
            <head>
                <title>Test de la fonction call-template</title>
            </head>
            <body>
                <xsl:for-eachpython manage.py runserver select="repertoire/personne">
                    <xsl:call-template name="afficherNom">
                        <xsl:with-param name="nomFamille" select="nom"/>
                    </xsl:call-template>
                </xsl:for-eachpython>
            </body>
        </html>
    </xsl:template>

    <xsl:template name="afficherNom">
        <xsl:param name="nomFamille"/>
        <xsl:param name="constante">nom de la personne</xsl:param>
        <p><xsl:value-of select="$constante"/>:
            <xsl:value-of select="$nomFamille"/>
        </p>

    </xsl:template>

</xsl:stylesheet>