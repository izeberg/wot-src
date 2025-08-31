package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import net.wg.infrastructure.interfaces.IMovieClip;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public interface IGunMarkerDispersion extends IMovieClip, IDisposable
   {
       
      
      function setAlpha(param1:Number, param2:Boolean) : void;
      
      function setReloadingParams(param1:Number, param2:String) : void;
      
      function setThickness(param1:String) : void;
      
      function setType(param1:Number) : void;
   }
}
