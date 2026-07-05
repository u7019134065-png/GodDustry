// Localize the mod's own display name and description from the active bundle.
var mod = Vars.mods.locateMod("goddustry");
if(mod != null){
    mod.meta.displayName = Core.bundle.get("mod.goddustry.displayName", mod.meta.displayName);
    mod.meta.description = Core.bundle.get("mod.goddustry.description", mod.meta.description);
}
