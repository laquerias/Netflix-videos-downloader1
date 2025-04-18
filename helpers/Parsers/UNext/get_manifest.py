from helpers.ripprocess import ripprocess
from helpers.Parsers.Netflix.MSLClient import MSLClient
from configs.config import tool
import xml.etree.ElementTree as ET
import re, os, json, logging

def MSLprofiles():
	PROFILES = {
		"BASICS": ["BIF240", "BIF320", "webvtt-lssdh-ios8", "dfxp-ls-sdh"],
		"MAIN": {
			"SD": [
				"playready-h264bpl30-dash",
				"playready-h264mpl22-dash",
				"playready-h264mpl30-dash",
			],
			"HD": [
				"playready-h264bpl30-dash",
				"playready-h264mpl22-dash",
				"playready-h264mpl30-dash",
				"playready-h264mpl31-dash",
			],
			"FHD": [
				"playready-h264bpl30-dash",
				"playready-h264mpl22-dash",
				"playready-h264mpl30-dash",
				"playready-h264mpl31-dash",
				"playready-h264mpl40-dash",
			],
			"ALL": [
				"playready-h264bpl30-dash",
				"playready-h264mpl22-dash",
				"playready-h264mpl30-dash",
				"playready-h264mpl31-dash",
				"playready-h264mpl40-dash",
			],
		},
		"MAIN480": {
			"SD": [
				"playready-h264bpl30-dash",
				"playready-h264mpl22-dash",
				"playready-h264mpl30-dash",
			],
			"ALL": [
				"playready-h264bpl30-dash",
				"playready-h264mpl22-dash",
				"playready-h264mpl30-dash",
			],
		},
		"HIGH": {
			"SD": [
				"playready-h264hpl22-dash",
				"playready-h264hpl30-dash",
			],
			"HD": [
				"playready-h264hpl22-dash",
				"playready-h264hpl30-dash",
				"playready-h264hpl31-dash",
			],
			"FHD": [
				"playready-h264hpl22-dash",
				"playready-h264hpl30-dash",
				"playready-h264hpl31-dash",
				"playready-h264hpl40-dash",
			],
			"ALL": [
				"playready-h264hpl22-dash",
				"playready-h264hpl30-dash",
				"playready-h264hpl31-dash",
				"playready-h264hpl40-dash",
			],
		},
		"HEVC": {
			"SD": [
				"hevc-main-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc-prk",
			],
			"HD": [
				"hevc-main-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc-prk",
				"hevc-main-L31-dash-cenc",
				"hevc-main10-L31-dash-cenc",
				"hevc-main10-L31-dash-cenc-prk",
			],
			"FHD": [
				"hevc-main-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc-prk",
				"hevc-main-L31-dash-cenc"
				"hevc-main10-L31-dash-cenc",
				"hevc-main10-L31-dash-cenc-prk",
				"hevc-main-L40-dash-cenc",				
				"hevc-main10-L40-dash-cenc",
				"hevc-main10-L40-dash-cenc-prk",
				"hevc-main-L41-dash-cenc",				
				"hevc-main10-L41-dash-cenc",
				"hevc-main10-L41-dash-cenc-prk",
			],
			"ALL": [
				"hevc-main-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc",
				"hevc-main10-L30-dash-cenc-prk",
				"hevc-main-L31-dash-cenc"
				"hevc-main10-L31-dash-cenc",
				"hevc-main10-L31-dash-cenc-prk",
				"hevc-main-L40-dash-cenc",				
				"hevc-main10-L40-dash-cenc",
				"hevc-main10-L40-dash-cenc-prk",				
				"hevc-main-L41-dash-cenc",				
				"hevc-main10-L41-dash-cenc",
				"hevc-main10-L41-dash-cenc-prk",
			],
		},
		"HEVCDO": {
			"SD": [
				"hevc-main10-L30-dash-cenc-prk-do",
			],
			"HD": [
				"hevc-main10-L30-dash-cenc-prk-do",
				"hevc-main10-L31-dash-cenc-prk-do"
			],
			"FHD": [
				"hevc-main10-L31-dash-cenc-prk-do",
				"hevc-main10-L31-dash-cenc-prk-do",
				"hevc-main10-L40-dash-cenc-prk-do",
				"hevc-main10-L41-dash-cenc-prk-do",
			],
			"ALL": [
				"hevc-main10-L31-dash-cenc-prk-do",
				"hevc-main10-L31-dash-cenc-prk-do",
				"hevc-main10-L40-dash-cenc-prk-do",
				"hevc-main10-L41-dash-cenc-prk-do",
			],
		},				
		"HDR": {
			"SD": [
				"hevc-hdr-main10-L30-dash-cenc",
				"hevc-hdr-main10-L30-dash-cenc-prk",
			],
			"HD": [
				"hevc-hdr-main10-L30-dash-cenc",
				"hevc-hdr-main10-L30-dash-cenc-prk",
				"hevc-hdr-main10-L31-dash-cenc",
				"hevc-hdr-main10-L31-dash-cenc-prk",
			],
			"FHD": [
				"hevc-hdr-main10-L30-dash-cenc",
				"hevc-hdr-main10-L30-dash-cenc-prk",
				"hevc-hdr-main10-L31-dash-cenc",
				"hevc-hdr-main10-L31-dash-cenc-prk",
				"hevc-hdr-main10-L40-dash-cenc",
				"hevc-hdr-main10-L41-dash-cenc",
				"hevc-hdr-main10-L40-dash-cenc-prk",
				"hevc-hdr-main10-L41-dash-cenc-prk",
			],
			"ALL": [
				"hevc-hdr-main10-L30-dash-cenc",
				"hevc-hdr-main10-L30-dash-cenc-prk",
				"hevc-hdr-main10-L31-dash-cenc",
				"hevc-hdr-main10-L31-dash-cenc-prk",
				"hevc-hdr-main10-L40-dash-cenc",
				"hevc-hdr-main10-L41-dash-cenc",
				"hevc-hdr-main10-L40-dash-cenc-prk",
				"hevc-hdr-main10-L41-dash-cenc-prk",
			],
		},
	}

	return PROFILES

class UNextManifestParser:
    def __init__(self, mpd_content):
        self.tree = ET.ElementTree(ET.fromstring(mpd_content))

    def parse(self):
        streams = []
        for adaptation_set in self.tree.findall(".//AdaptationSet"):
            stream_type = adaptation_set.attrib.get("contentType")
            for representation in adaptation_set.findall("Representation"):
                base_url = representation.find("BaseURL").text
                streams.append({"type": stream_type, "url": base_url})
        return streams