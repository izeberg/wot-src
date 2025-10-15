package net.wg.portal.gui.battle.minimap
{
   import flash.events.Event;
   import net.wg.gui.battle.views.minimap.EpicMinimap;
   
   public class PortalMinimap extends EpicMinimap
   {
      
      public static const TAB_MODE_502_IDX:int = EpicMinimap.TAB_MODE_502_IDX;
      
      public static const TAB_MODE_700_IDX:int = EpicMinimap.TAB_MODE_700_IDX;
      
      private static const MAP_SHORTCUT_LABEL_SCALE_SMALL:Number = 0.53;
      
      private static const MAP_SHORTCUT_LABEL_SCALE_MEDIUM:Number = 0.78;
      
      private static const MAP_SHORTCUT_LABEL_NO_SCALE:Number = 1;
      
      private static const SIZE_INDEX_TO_SCALE:Array = [MAP_SHORTCUT_LABEL_SCALE_SMALL,MAP_SHORTCUT_LABEL_SCALE_SMALL,MAP_SHORTCUT_LABEL_SCALE_SMALL,MAP_SHORTCUT_LABEL_SCALE_MEDIUM,MAP_SHORTCUT_LABEL_SCALE_MEDIUM,MAP_SHORTCUT_LABEL_NO_SCALE,MAP_SHORTCUT_LABEL_NO_SCALE,MAP_SHORTCUT_LABEL_NO_SCALE];
       
      
      public function PortalMinimap()
      {
         super();
         mapShortcutLabel.sectorOverview.visible = false;
         mapShortcutLabel.mapBtnTF.visible = false;
      }
      
      override public function setAllowedSizeIndex(param1:Number) : void
      {
         super.setAllowedSizeIndex(param1);
         mapShortcutLabel.scaleX = mapShortcutLabel.scaleY = SIZE_INDEX_TO_SCALE[param1];
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      override public function toggleTabMode(param1:Boolean) : void
      {
         super.toggleTabMode(param1);
         mapShortcutLabel.visible = !this.isTabMode;
      }
   }
}
