#!/usr/bin/env python3
# Created: Dec, 06, 2024 23:26:26 by Wataru Fukuda

import numpy
import os

class MeshFactory:
  def __init__(self, cfg, config_path):
    self.cfg = cfg
    self.config_path = config_path
  def newInstance(self):
    return Mesh(self.cfg, self.config_path)

class Mesh:
  def __init__(self, cfg, config_path):
    self.cfg = cfg
    self.config_dir = os.path.dirname(config_path)
    self.nn = cfg.get("nn")
    self.ne = cfg.get("ne")
    self.nsd = cfg.get("nsd")
    self.npd = cfg.get("npd")
    self.nen = cfg.get("nen")
    self.endian = cfg.get("endian")
    self.xyz_file = os.path.join(self.config_dir, cfg.get("xyz"))
    self.ien_file = os.path.join(self.config_dir, cfg.get("ien"))
    self.rng_file = os.path.join(self.config_dir, cfg.get("rng"))
    self.rng = cfg.get("rng")
  def getNumberOfNodes(self):
    return self.nn
  def getNumberOfElements(self):
    return self.ne
  def getNumberOfSpatialDimensions(self):
    return self.nsd
  def getNumberOfParametricDimensions(self):
    return self.npd
  def getOrder(self):
    return [[self.nen]]
  def getEndian(self):
    return self.endian
  def getOffset(self):
    return self.offset
  def getPositionFilePath(self):
    return self.xyz_file
  def getConnectivityFile(self):
    return self.ien_file
  def getRngFile(self):
    return self.rng
  def getDomainType(self):
    return self.domain_type
  def getPosition(self):
    positions = numpy.fromfile(self.xyz_file, dtype=">f8").reshape((self.nn,self.nsd))
    return positions
  def getIen(self):
    connectivity = numpy.fromfile(self.ien_file, dtype=">i4").reshape((self.ne,self.nen))
    return connectivity
  def getRng(self):
    boundary = numpy.fromfile(self.rng_file, dtype=">i4").reshape((self.ne,self.nen))
    return boundary

