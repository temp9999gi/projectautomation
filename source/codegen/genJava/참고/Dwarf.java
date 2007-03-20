// Dwarf.java

public class Dwarf{
  privateint dwarfId;
  privateString dwarfName;
  privateint born;
  privateint homeId;
  privateString homeName;
  privateint spouseId;
  privateString spouseName;

  public Dwarf(
    int dwarfId,
    String dwarfName,
    int born,
    int homeId,
    String homeName,
    int spouseId,
    String spouseName)
  {
    this.dwarfId = dwarfId;
    this.dwarfName = dwarfName;
    this.born = born;
    this.homeId = homeId;
    this.homeName = homeName;
    this.spouseId = spouseId;
    this.spouseName = spouseName;
  }

  public Dwarf(){
    this.dwarfId = 0;
    this.dwarfName = null;
    this.born = 0;
    this.homeId = 0;
    this.homeName = null;
    this.spouseId = 0;
    this.spouseName = null;
  }

  public int getDwarfId() { return dwarfId; }
  public void setDwarfId(int dwarfId) { this.dwarfId = dwarfId; }

  public String getDwarfName() { return dwarfName; }
  public void setDwarfName(String dwarfName) { this.dwarfName = dwarfName; }

  public int getBorn() { return born; }
  public void setBorn(int born) { this.born = born; }

  public int getHomeId() { return homeId; }
  public void setHomeId(int homeId) { this.homeId = homeId; }

  public String getHomeName() { return homeName; }
  public void setHomeName(String homeName) { this.homeName = homeName; }

  public int getSpouseId() { return spouseId; }
  public void setSpouseId(int spouseId) { this.spouseId = spouseId; }

  public String getSpouseName() { return spouseName; }
  public void setSpouseName(String spouseName) { this.spouseName = spouseName; }

}
