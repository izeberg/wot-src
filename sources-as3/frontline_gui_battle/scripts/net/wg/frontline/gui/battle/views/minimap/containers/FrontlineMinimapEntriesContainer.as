package net.wg.frontline.gui.battle.views.minimap.containers
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.gui.battle.views.minimap.containers.MinimapEntriesContainer;
   import net.wg.gui.components.controls.UILoaderAlt;
   
   public class FrontlineMinimapEntriesContainer extends MinimapEntriesContainer
   {
       
      
      public var maskTop:MovieClip = null;
      
      public var hqs:Sprite = null;
      
      public var maskBottom:MovieClip = null;
      
      public var zones:Sprite = null;
      
      public var landingZone:Sprite = null;
      
      public var background:UILoaderAlt = null;
      
      public function FrontlineMinimapEntriesContainer()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.maskTop = null;
         this.hqs = null;
         this.maskBottom = null;
         this.zones = null;
         this.landingZone = null;
         this.background.dispose();
         this.background = null;
         super.onDispose();
      }
   }
}
