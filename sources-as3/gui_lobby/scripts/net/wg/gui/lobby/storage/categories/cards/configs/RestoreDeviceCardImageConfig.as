package net.wg.gui.lobby.storage.categories.cards.configs
{
   import flash.geom.Rectangle;
   import net.wg.utils.StageSizeBoundaries;
   
   public class RestoreDeviceCardImageConfig extends CardImageConfig
   {
       
      
      public function RestoreDeviceCardImageConfig()
      {
         super();
      }
      
      override public function initialize() : void
      {
         _imagesByResolution[StageSizeBoundaries.WIDTH_1024] = _imagesByResolution[StageSizeBoundaries.WIDTH_1366] = new CardImageSizeVO(new Rectangle(-1,-1,115,86),new Rectangle(-1,-1,115,86));
         _imagesByResolution[StageSizeBoundaries.WIDTH_1600] = _imagesByResolution[StageSizeBoundaries.WIDTH_1920] = new CardImageSizeVO(new Rectangle(-1,-1,144,108),new Rectangle(-1,-1,144,108));
      }
   }
}
